from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.models.entry import EntryStatus
from app.db.models.approval_log import ApprovalStatus
from app.db.repositories.entry_repo import EntryRepository
from app.db.repositories.approval_repo import ApprovalRepository

class ApprovalService:
    def __init__(self, db: Session):
        self.entry_repo = EntryRepository(db)
        self.approval_repo = ApprovalRepository(db)

    def list_pending_entries(self):
        # return entries with status = PENDING
        return self.entry_repo.db.query(self.entry_repo.db.query_property().class_).filter_by(status=EntryStatus.PENDING).all()

    def approve(self, entry_id: int, admin_id: int, remarks: str | None = None):
        entry = self.entry_repo.get_by_id(entry_id)
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")

        entry = self.entry_repo.update(entry, status=EntryStatus.APPROVED)
        self.approval_repo.create(entry_id, admin_id, ApprovalStatus.APPROVED, remarks)
        return entry

    def reject(self, entry_id: int, admin_id: int, remarks: str | None = None):
        entry = self.entry_repo.get_by_id(entry_id)
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")

        entry = self.entry_repo.update(entry, status=EntryStatus.REJECTED)
        self.approval_repo.create(entry_id, admin_id, ApprovalStatus.REJECTED, remarks)
        return entry
