from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain, hashed) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(subject: int, expires_delta: timedelta = None):
    now = datetime.utcnow()
    exp = now + (expires_delta or timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRES_MINUTES))
    payload = {"sub": str(subject), "exp": exp}
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_token(token: str):
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
