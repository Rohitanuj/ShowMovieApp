from pydantic_settings import BaseSettings, Field, HttpUrl
from typing import Optional
from datetime import datetime

class EntryCreate(BaseModel):
    title: str = Field(..., max_length=300)
    type: str   # "MOVIE" | "TV_SHOW"
    director: Optional[str]
    budget: Optional[float]
    location: Optional[str]
    duration_minutes: Optional[int]
    year_start: Optional[int]
    year_end: Optional[int]
    description: Optional[str]

class EntryUpdate(BaseModel):
    title: Optional[str]
    director: Optional[str]
    budget: Optional[float]
    location: Optional[str]
    duration_minutes: Optional[int]
    year_start: Optional[int]
    year_end: Optional[int]
    description: Optional[str]
    # updating image handled via uploads endpoint

class EntryOut(BaseModel):
    id: int
    title: str
    type: str
    director: Optional[str]
    budget: Optional[float]
    location: Optional[str]
    duration_minutes: Optional[int]
    year_start: Optional[int]
    year_end: Optional[int]
    description: Optional[str]
    image_url: Optional[HttpUrl]
    thumb_url: Optional[HttpUrl]
    status: str
    created_by: int
    created_at: datetime

    class Config:
        orm_mode = True
