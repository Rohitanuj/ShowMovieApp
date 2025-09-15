# backend/app/api/v1/uploads.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from ..deps import get_current_user
from ...utils.s3 import upload_fileobj
from ...utils.image import make_thumbnail

router = APIRouter(prefix="/uploads", tags=["uploads"])

@router.post("/image")
async def upload_image(file: UploadFile = File(...), user=Depends(get_current_user)):
    if file.content_type not in {"image/jpeg","image/png","image/webp"}:
        raise HTTPException(400, "Invalid image type")
    if file.size and file.size > 5*1024*1024:
        raise HTTPException(400, "File too large")

    original_bytes = await file.read()
    thumb_bytes = make_thumbnail(original_bytes, max_size=360)

    url = upload_fileobj(original_bytes, key_prefix=f"entries/{user.id}/")
    thumb_url = upload_fileobj(thumb_bytes, key_prefix=f"entries/{user.id}/thumbs/")

    return {"image_url": url, "thumb_url": thumb_url}
