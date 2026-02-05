from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_current_user, get_db
from app.schemas.user import UserOut, UserUpdate
from app.crud import user as user_crud

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_me(current_user=Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserOut)
def update_me(payload: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    updated = user_crud.update(db, current_user, payload)
    return updated
