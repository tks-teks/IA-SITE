from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db, require_role
from app.models.user import User
from app.models.project import Project
from app.schemas.user import UserOut, UserUpdate
from app.schemas.log import AuditLogOut
from app.crud import user as user_crud
from app.crud import log as log_crud

router = APIRouter()


@router.get("/stats")
def stats(db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    users_count = db.query(User).count()
    projects_count = db.query(Project).count()
    return {"users": users_count, "projects": projects_count}


@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return db.query(User).all()


@router.put("/users/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("admin")),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated = user_crud.update(db, user, payload)
    log_crud.create(db, current_user.email, "admin_update", f"user:{user.id}")
    return updated


@router.get("/logs", response_model=list[AuditLogOut])
def list_logs(skip: int = 0, limit: int = 20, db: Session = Depends(get_db), current_user=Depends(require_role("admin"))):
    return log_crud.list(db, skip=skip, limit=limit)
