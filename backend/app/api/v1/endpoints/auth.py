from datetime import datetime, timedelta
import uuid
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import create_access_token, create_refresh_token, verify_password
from app.core.deps import get_db
from app.crud import user as user_crud
from app.models.refresh_token import RefreshToken
from app.schemas.auth import Token
from app.schemas.user import UserCreate, UserOut
from app.services.rate_limit import limiter

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    existing = user_crud.get_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = user_crud.create(db, payload)
    return user


@router.post("/login", response_model=Token)
@limiter.limit("5/minute")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.get_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    access_token = create_access_token(user.email, user.role)
    refresh_jti = str(uuid.uuid4())
    refresh_token = create_refresh_token(user.email, user.role, refresh_jti)
    expires_at = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    db.add(RefreshToken(jti=refresh_jti, user_id=user.id, expires_at=expires_at))
    db.commit()
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh", response_model=Token)
def refresh(token: str, db: Session = Depends(get_db)):
    from jose import jwt, JWTError

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid refresh token") from exc

    stored = db.query(RefreshToken).filter(RefreshToken.jti == payload.get("jti")).first()
    if not stored or stored.revoked or stored.expires_at < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Refresh token expired")

    user = user_crud.get_by_email(db, payload.get("sub"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    stored.revoked = True
    db.add(stored)
    db.commit()

    access_token = create_access_token(user.email, user.role)
    new_jti = str(uuid.uuid4())
    refresh_token = create_refresh_token(user.email, user.role, new_jti)
    expires_at = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    db.add(RefreshToken(jti=new_jti, user_id=user.id, expires_at=expires_at))
    db.commit()

    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post("/logout")
def logout(token: str, db: Session = Depends(get_db)):
    from jose import jwt, JWTError

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc

    stored = db.query(RefreshToken).filter(RefreshToken.jti == payload.get("jti")).first()
    if stored:
        stored.revoked = True
        db.add(stored)
        db.commit()
    return {"status": "logged_out"}
