from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash


def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create(db: Session, obj_in: UserCreate):
    user = User(
        email=obj_in.email,
        full_name=obj_in.full_name,
        hashed_password=get_password_hash(obj_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User, obj_in: UserUpdate):
    data = obj_in.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(user, field, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
