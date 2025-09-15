from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.repositories.user_repo import UserRepository
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token  # you will add this in utils or core

class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def signup(self, username: str, email: str, password: str):
        if self.user_repo.get_by_username(username) or self.user_repo.get_by_email(email):
            raise HTTPException(status_code=400, detail="Duplicate user/email")
        user = self.user_repo.create(username, email, hash_password(password))
        return user

    def login(self, username_or_email: str, password: str):
        user = (
            self.user_repo.get_by_username(username_or_email)
            or self.user_repo.get_by_email(username_or_email)
        )
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        token = create_access_token({"sub": str(user.id), "role": user.role})
        return {"access_token": token, "token_type": "bearer"}
