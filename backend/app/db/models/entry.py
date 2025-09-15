import enum
from sqlalchemy import Column, Integer, String, Enum, Numeric, DateTime, ForeignKey, Text, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class EntryType(str, enum.Enum):
    MOVIE = "MOVIE"
    TV_SHOW = "TV_SHOW"

class EntryStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False, index=True)
    type = Column(Enum(EntryType), nullable=False, index=True)
    director = Column(String(200), index=True)
    budget = Column(Numeric(14,2), nullable=True)
    location = Column(String(200), nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    year_start = Column(Integer, nullable=True)
    year_end = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String(1024), nullable=True)
    thumb_url = Column(String(1024), nullable=True)
    status = Column(Enum(EntryStatus), nullable=False, default=EntryStatus.PENDING, index=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    author = relationship("User", back_populates="entries")
    approvals = relationship("ApprovalLog", back_populates="entry", cascade="all, delete-orphan")

    __table_args__ = (
        Index('ix_entries_title_trgm', 'title'),  # for trigram extension (PG)
    )
