from sqlalchemy.orm import Session
from app.db.models.approval_log import ApprovalLog, ApprovalStatus

class ApprovalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, entry_id: int, admin_id: int, status: ApprovalStatus, remarks: str | None = None) -> ApprovalLog:
        log = ApprovalLog(entry_id=entry_id, admin_id=admin_id, status=status, remarks=remarks)
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log

    def list_by_entry(self, entry_id: int) -> list[ApprovalLog]:
        return self.db.query(ApprovalLog).filter(ApprovalLog.entry_id == entry_id).all()
