from pydantic import BaseModel
from typing import List, Optional


class GenerateRequest(BaseModel):
    project_name: str
    description: str
    primary_resource: str
    roles: List[str] = ["admin", "user"]
    theme: Optional[str] = "dark"
    stack: Optional[str] = "fastapi-react"


class GeneratedFile(BaseModel):
    path: str
    content: str


class GenerateResponse(BaseModel):
    project_slug: str
    summary: str
    files: List[GeneratedFile]
