from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import Optional, List
from app.api.deps import get_current_user, admin_required
from app.schemas.entry import EntryCreate, EntryUpdate, EntryOut

router = APIRouter(prefix="/entries", tags=["entries"])


@router.post("", response_model=EntryOut, status_code=201)
def create_entry(payload: EntryCreate, user=Depends(get_current_user)):
    # TODO: insert into DB with status=PENDING, created_by=user.id
    return {"id": 1, "title": payload.title, "status": "PENDING", "created_by": user.id}


@router.get("", response_model=List[EntryOut])
def list_entries(
    q: Optional[str] = None,
    type: Optional[str] = Query(None, regex="^(MOVIE|TV_SHOW)$"),
    director: Optional[str] = None,
    year_min: Optional[int] = None,
    year_max: Optional[int] = None,
    sort: str = Query("created_at"),
    order: str = Query("desc", regex="^(asc|desc)$"),
    limit: int = Query(20, ge=1, le=100),
    cursor: Optional[str] = None,
):
    # TODO: query only APPROVED entries, apply filters + pagination
    return []


@router.get("/mine", response_model=List[EntryOut])
def list_my_entries(user=Depends(get_current_user)):
    # TODO: return all entries created_by=user.id (all statuses, excluding soft-deleted)
    return []


@router.get("/{entry_id}", response_model=EntryOut)
def get_entry(entry_id: int, user=Depends(get_current_user)):
    # TODO: enforce visibility rules (APPROVED=public, others only owner/admin)
    raise HTTPException(status_code=404, detail="Entry not found")


@router.put("/{entry_id}", response_model=EntryOut)
def update_entry(entry_id: int, payload: EntryUpdate, user=Depends(get_current_user)):
    # TODO: owner or admin can update
    return {"id": entry_id, **payload.dict(exclude_unset=True)}


@router.delete("/{entry_id}", status_code=204)
def delete_entry(entry_id: int, user=Depends(get_current_user)):
    # TODO: soft delete (set deleted_at)
    return
