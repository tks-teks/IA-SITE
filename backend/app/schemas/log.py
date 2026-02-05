from pydantic import BaseModel
from datetime import datetime


class AuditLogOut(BaseModel):
    id: int
    actor_email: str
    action: str
    target: str
    created_at: datetime

    class Config:
        orm_mode = True
