from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)

    tracks = relationship("Track", back_populates="genre", cascade="all, delete")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    artist_name = Column(String(200), nullable=False, index=True)
    album_title = Column(String(200), nullable=True)
    duration_seconds = Column(Integer, nullable=True)
    mood = Column(String(100), nullable=True)
    play_count = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)

    genre = relationship("Genre", back_populates="tracks")
    reviews = relationship("Review", back_populates="track", cascade="all, delete-orphan")
    tags = relationship("UserTag", back_populates="track", cascade="all, delete-orphan")
    collection_items = relationship("CollectionItem", back_populates="track", cascade="all, delete-orphan")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False, index=True)
    reviewer_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    track = relationship("Track", back_populates="reviews")


class UserTag(Base):
    __tablename__ = "user_tags"
    __table_args__ = (UniqueConstraint("track_id", "tag_name", name="uq_track_tag_name"),)

    id = Column(Integer, primary_key=True, index=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False, index=True)
    tag_name = Column(String(50), nullable=False, index=True)
    created_by = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    track = relationship("Track", back_populates="tags")


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
    created_by = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    items = relationship("CollectionItem", back_populates="collection", cascade="all, delete-orphan")


class CollectionItem(Base):
    __tablename__ = "collection_items"
    __table_args__ = (UniqueConstraint("collection_id", "track_id", name="uq_collection_track"),)

    id = Column(Integer, primary_key=True, index=True)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=False, index=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False, index=True)
    note = Column(Text, nullable=True)

    collection = relationship("Collection", back_populates="items")
    track = relationship("Track", back_populates="collection_items")
