from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from app.db.models.entry import EntryStatus
from app.db.repositories.entry_repo import EntryRepository

class EntryService:
    def __init__(self, db: Session):
        self.entry_repo = EntryRepository(db)

    def create_entry(self, data: dict, user_id: int):
        data["created_by"] = user_id
        data["status"] = EntryStatus.PENDING
        return self.entry_repo.create(**data)

    def list_public_entries(self, limit: int = 20, offset: int = 0):
        return self.entry_repo.list_public(limit=limit, offset=offset)

    def list_user_entries(self, user_id: int):
        return self.entry_repo.list_by_user(user_id)

    def get_entry(self, entry_id: int, user: dict):
        entry = self.entry_repo.get_by_id(entry_id)
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")

        if entry.status == EntryStatus.APPROVED:
            return entry
        if entry.created_by == user["id"] or user["role"] == "ADMIN":
            return entry

        raise HTTPException(status_code=404, detail="Entry not found")

    def update_entry(self, entry_id: int, data: dict, user: dict):
        entry = self.entry_repo.get_by_id(entry_id)
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")

        if user["role"] != "ADMIN" and entry.created_by != user["id"]:
            raise HTTPException(status_code=403, detail="Forbidden")

        return self.entry_repo.update(entry, **data)

    def delete_entry(self, entry_id: int, user: dict):
        entry = self.entry_repo.get_by_id(entry_id)
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")

        if user["role"] != "ADMIN" and entry.created_by != user["id"]:
            raise HTTPException(status_code=403, detail="Forbidden")

        self.entry_repo.soft_delete(entry)
        return
