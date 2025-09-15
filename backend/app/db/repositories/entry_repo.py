from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
from datetime import datetime
from app.db.models.entry import Entry, EntryStatus, EntryType

class EntryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, **kwargs) -> Entry:
        entry = Entry(**kwargs)
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def get_by_id(self, entry_id: int) -> Entry | None:
        return self.db.query(Entry).filter(
            Entry.id == entry_id, Entry.deleted_at.is_(None)
        ).first()

    def list_public(self, limit: int = 20, offset: int = 0) -> List[Entry]:
        return (
            self.db.query(Entry)
            .filter(Entry.status == EntryStatus.APPROVED, Entry.deleted_at.is_(None))
            .order_by(Entry.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

    def list_by_user(self, user_id: int) -> List[Entry]:
        return (
            self.db.query(Entry)
            .filter(Entry.created_by == user_id, Entry.deleted_at.is_(None))
            .order_by(Entry.created_at.desc())
            .all()
        )

    def update(self, entry: Entry, **kwargs) -> Entry:
        for key, value in kwargs.items():
            setattr(entry, key, value)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def soft_delete(self, entry: Entry) -> None:
        entry.deleted_at = datetime.utcnow()
        self.db.commit()
