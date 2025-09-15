from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .base import Base

class ApprovalStatus(str, enum.Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class ApprovalLog(Base):
    __tablename__ = "approval_logs"
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey("entries.id"), nullable=False, index=True)
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(ApprovalStatus), nullable=False)
    remarks = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    entry = relationship("Entry", back_populates="approvals")
    admin = relationship("User")
