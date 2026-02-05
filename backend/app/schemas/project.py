from pydantic import BaseModel
from typing import Optional


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = "draft"
    image_url: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    image_url: Optional[str] = None


class ProjectOut(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
