import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.core.deps import get_current_user, get_db
from app.core.config import settings
from app.schemas.project import ProjectOut, ProjectCreate, ProjectUpdate
from app.crud import project as project_crud
from app.crud import log as log_crud

router = APIRouter()


@router.post("/", response_model=ProjectOut)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    project = project_crud.create(db, payload, owner_id=current_user.id)
    log_crud.create(db, current_user.email, "create", f"project:{project.id}")
    return project


@router.get("/", response_model=list[ProjectOut])
def list_projects(
    skip: int = 0,
    limit: int = 10,
    query: str | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return project_crud.list(db, current_user.id, skip=skip, limit=limit, query=query)


@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    project = project_crud.get(db, project_id)
    if not project or project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{project_id}", response_model=ProjectOut)
def update_project(
    project_id: int,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    project = project_crud.get(db, project_id)
    if not project or project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Project not found")
    updated = project_crud.update(db, project, payload)
    log_crud.create(db, current_user.email, "update", f"project:{project.id}")
    return updated


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    project = project_crud.get(db, project_id)
    if not project or project.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Project not found")
    project_crud.delete(db, project)
    log_crud.create(db, current_user.email, "delete", f"project:{project.id}")
    return {"status": "deleted"}


@router.post("/upload")
def upload_image(file: UploadFile = File(...)):
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    file_location = os.path.join(settings.UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    return {"image_url": file_location}
