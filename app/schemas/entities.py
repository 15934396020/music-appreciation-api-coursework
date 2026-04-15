"""Pydantic schemas for request validation and response serialisation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Genre
# ---------------------------------------------------------------------------

class GenreRead(BaseModel):
    """Schema for genre responses."""
    id: int
    name: str
    description: Optional[str] = None

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Track
# ---------------------------------------------------------------------------

class TrackRead(BaseModel):
    """Schema for track responses (includes nested genre)."""
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


# ---------------------------------------------------------------------------
# Review
# ---------------------------------------------------------------------------

class ReviewCreate(BaseModel):
    """Schema for creating a new review."""
    track_id: int
    reviewer_name: str = Field(min_length=1, max_length=100, examples=["Alice"])
    rating: int = Field(ge=1, le=5, examples=[4])
    comment: str = Field(min_length=3, max_length=1000, examples=["A beautiful and moving piece."])


class ReviewUpdate(BaseModel):
    """Schema for updating an existing review (all fields optional)."""
    reviewer_name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = Field(default=None, min_length=3, max_length=1000)


class ReviewRead(BaseModel):
    """Schema for review responses."""
    id: int
    track_id: int
    reviewer_name: str
    rating: int
    comment: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------

class UserTagCreate(BaseModel):
    """Schema for creating a new user tag."""
    track_id: int
    tag_name: str = Field(min_length=1, max_length=50, examples=["melancholic"])
    created_by: str = Field(min_length=1, max_length=100, examples=["Alice"])


class UserTagRead(BaseModel):
    """Schema for user tag responses."""
    id: int
    track_id: int
    tag_name: str
    created_by: str
    created_at: datetime

    model_config = {"from_attributes": True}


class TagRead(BaseModel):
    """Simplified tag read schema for analytics."""
    tag_name: str
    usage_count: int

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Collections
# ---------------------------------------------------------------------------

class CollectionCreate(BaseModel):
    """Schema for creating a new collection."""
    name: str = Field(min_length=1, max_length=100, examples=["Evening Chill"])
    description: Optional[str] = Field(default=None, max_length=500, examples=["Tracks for winding down."])
    created_by: str = Field(min_length=1, max_length=100, examples=["Alice"])


class CollectionItemCreate(BaseModel):
    """Schema for adding a track to a collection."""
    track_id: int
    note: Optional[str] = Field(default=None, max_length=500, examples=["Great opening track."])


class CollectionRead(BaseModel):
    """Schema for collection list responses."""
    id: int
    name: str
    description: Optional[str] = None
    created_by: str
    created_at: datetime

    model_config = {"from_attributes": True}
