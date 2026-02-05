from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog


def create(db: Session, actor_email: str, action: str, target: str):
    log = AuditLog(actor_email=actor_email, action=action, target=target)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def list(db: Session, skip: int, limit: int):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()
