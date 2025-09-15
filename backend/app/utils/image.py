from io import BytesIO
from PIL import Image

def make_thumbnail(image_bytes: bytes, max_size: int = 360) -> bytes:
    """
    Create thumbnail from image bytes.
    Returns thumbnail as bytes.
    """
    with Image.open(BytesIO(image_bytes)) as img:
        img.thumbnail((max_size, max_size))
        out = BytesIO()
        img.save(out, format=img.format or "JPEG")
        return out.getvalue()
