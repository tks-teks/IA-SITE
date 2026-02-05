from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base_class import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    actor_email = Column(String, nullable=False)
    action = Column(String, nullable=False)
    target = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
