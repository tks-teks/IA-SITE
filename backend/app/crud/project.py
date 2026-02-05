from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


def create(db: Session, obj_in: ProjectCreate, owner_id: int):
    project = Project(**obj_in.dict(), owner_id=owner_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def list(db: Session, owner_id: int, skip: int, limit: int, query: str | None = None):
    q = db.query(Project).filter(Project.owner_id == owner_id)
    if query:
        q = q.filter(or_(Project.name.ilike(f"%{query}%"), Project.description.ilike(f"%{query}%")))
    return q.offset(skip).limit(limit).all()


def update(db: Session, project: Project, obj_in: ProjectUpdate):
    data = obj_in.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(project, field, value)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def delete(db: Session, project: Project):
    db.delete(project)
    db.commit()
