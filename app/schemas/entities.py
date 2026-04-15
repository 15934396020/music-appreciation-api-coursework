from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class GenreRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


class TrackRead(BaseModel):
    id: int
    title: str
    artist_name: str
    album_title: Optional[str] = None
    duration_seconds: Optional[int] = None
    mood: Optional[str] = None
    play_count: int
    average_rating: float
    genre: GenreRead

    model_config = {"from_attributes": True}


class ReviewCreate(BaseModel):
    track_id: int
    reviewer_name: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=1, le=5)
    comment: str = Field(min_length=3, max_length=1000)


class ReviewUpdate(BaseModel):
    reviewer_name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = Field(default=None, min_length=3, max_length=1000)


class ReviewRead(BaseModel):
    id: int
    track_id: int
    reviewer_name: str
    rating: int
    comment: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserTagCreate(BaseModel):
    track_id: int
    tag_name: str = Field(min_length=1, max_length=50)
    created_by: str = Field(min_length=1, max_length=100)


class UserTagRead(BaseModel):
    id: int
    track_id: int
    tag_name: str
    created_by: str
    created_at: datetime

    model_config = {"from_attributes": True}


class CollectionCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    created_by: str = Field(min_length=1, max_length=100)


class CollectionItemCreate(BaseModel):
    track_id: int
    note: Optional[str] = Field(default=None, max_length=500)


class CollectionRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_by: str
    created_at: datetime

    model_config = {"from_attributes": True}
