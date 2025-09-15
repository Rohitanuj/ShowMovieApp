from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.deps import admin_required
from app.schemas.entry import EntryOut
from app.schemas.approval import ApprovalIn

router = APIRouter(prefix="/admin/entries", tags=["admin"])


@router.get("/pending", response_model=List[EntryOut])
def list_pending_entries(admin=Depends(admin_required)):
    # TODO: return all entries with status=PENDING
    return []


@router.put("/{entry_id}/approve", response_model=EntryOut)
def approve_entry(entry_id: int, body: ApprovalIn, admin=Depends(admin_required)):
    # TODO: update entry.status=APPROVED, log approval
    return {"id": entry_id, "status": "APPROVED"}


@router.put("/{entry_id}/reject", response_model=EntryOut)
def reject_entry(entry_id: int, body: ApprovalIn, admin=Depends(admin_required)):
    # TODO: update entry.status=REJECTED, log rejection
    return {"id": entry_id, "status": "REJECTED", "remarks": body.remarks}


@router.delete("/{entry_id}", status_code=204)
def delete_entry_admin(entry_id: int, admin=Depends(admin_required)):
    # TODO: admin can hard or soft delete
    return
