# from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from app.api.deps import get_current_user
from app.schemas.user import UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

# Schemas
class SignupIn(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginIn(BaseModel):
    username_or_email: str
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/signup", response_model=UserOut, status_code=201)
def signup(payload: SignupIn):
    # TODO: check duplicate user/email in DB
    # TODO: hash password and save user
    # return created user
    raise HTTPException(status_code=400, detail="Duplicate user/email")


@router.post("/login", response_model=TokenOut)
def login(payload: LoginIn):
    # TODO: validate username_or_email + password
    # TODO: issue JWT token
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/me", response_model=UserOut)
def me(current_user=Depends(get_current_user)):
    return current_user
