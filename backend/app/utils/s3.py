import boto3
import uuid
from app.core.config import settings

# expects in .env:
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET, S3_REGION

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=getattr(settings, "S3_REGION", "us-east-1"),
)

def upload_fileobj(file_bytes: bytes, key_prefix: str = "uploads/") -> str:
    """
    Upload a file-like object to S3/MinIO and return its URL.
    """
    key = f"{key_prefix}{uuid.uuid4().hex}"
    bucket = settings.S3_BUCKET
    s3_client.put_object(Bucket=bucket, Key=key, Body=file_bytes, ContentType="image/jpeg")
    url = f"https://{bucket}.s3.{settings.S3_REGION}.amazonaws.com/{key}"
    return url
