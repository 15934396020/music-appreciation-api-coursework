"""API router — all endpoint definitions for the Music Appreciation and Discovery API."""

from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from app.database import get_db
from app.models.entities import Collection, CollectionItem, Genre, Review, Track, UserTag
from app.schemas.entities import (
    CollectionCreate,
    CollectionItemCreate,
    CollectionRead,
    GenreRead,
    ReviewCreate,
    ReviewRead,
    ReviewUpdate,
    TagRead,
    TrackRead,
    UserTagCreate,
    UserTagRead,
)

router = APIRouter()


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _refresh_track_rating(db: Session, track_id: int) -> None:
    """Recalculate and persist the average rating for a given track."""
    avg_rating = (
        db.query(func.avg(Review.rating))
        .filter(Review.track_id == track_id)
        .scalar()
    )
    track = db.query(Track).filter(Track.id == track_id).first()
    if track:
        track.average_rating = round(float(avg_rating), 2) if avg_rating is not None else 0.0
        db.add(track)
        db.commit()


# ---------------------------------------------------------------------------
# Genres
# ---------------------------------------------------------------------------

@router.get("/genres", response_model=list[GenreRead], tags=["Genres"])
def list_genres(db: Session = Depends(get_db)):
    """Return all genres ordered alphabetically."""
    return db.query(Genre).order_by(Genre.name.asc()).all()


@router.get("/genres/{genre_id}", response_model=GenreRead, tags=["Genres"])
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    """Return a single genre by its ID."""
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


# ---------------------------------------------------------------------------
# Tracks
# ---------------------------------------------------------------------------

@router.get("/tracks", response_model=list[TrackRead], tags=["Tracks"])
def list_tracks(
    title: str | None = Query(default=None, description="Filter tracks by title (partial match)"),
    artist: str | None = Query(default=None, description="Filter tracks by artist name (partial match)"),
    genre: str | None = Query(default=None, description="Filter tracks by genre name (partial match)"),
    mood: str | None = Query(default=None, description="Filter tracks by mood keyword (partial match)"),
    sort_by: str = Query(default="title", description="Sort field: title, artist, rating, play_count"),
    order: str = Query(default="asc", description="Sort order: asc or desc"),
    limit: int = Query(default=20, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(default=0, ge=0, description="Number of results to skip"),
    db: Session = Depends(get_db),
):
    """List tracks with optional filtering, sorting, and pagination."""
    query = db.query(Track).options(joinedload(Track.genre))

    if title:
        query = query.filter(Track.title.ilike(f"%{title}%"))
    if artist:
        query = query.filter(Track.artist_name.ilike(f"%{artist}%"))
    if genre:
        query = query.join(Genre).filter(Genre.name.ilike(f"%{genre}%"))
    if mood:
        query = query.filter(Track.mood.ilike(f"%{mood}%"))

    sort_columns = {
        "title": Track.title,
        "artist": Track.artist_name,
        "rating": Track.average_rating,
        "play_count": Track.play_count,
    }
    sort_col = sort_columns.get(sort_by, Track.title)
    query = query.order_by(sort_col.desc() if order == "desc" else sort_col.asc())

    return query.offset(offset).limit(limit).all()


@router.get("/tracks/{track_id}", response_model=TrackRead, tags=["Tracks"])
def get_track(track_id: int, db: Session = Depends(get_db)):
    """Return a single track by its ID."""
    track = (
        db.query(Track)
        .options(joinedload(Track.genre))
        .filter(Track.id == track_id)
        .first()
    )
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


# ---------------------------------------------------------------------------
# Reviews (main CRUD resource)
# ---------------------------------------------------------------------------

@router.post("/reviews", response_model=ReviewRead, status_code=status.HTTP_201_CREATED, tags=["Reviews"])
def create_review(payload: ReviewCreate, db: Session = Depends(get_db)):
    """Create a new review for a track."""
    track = db.query(Track).filter(Track.id == payload.track_id).first()
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    review = Review(**payload.model_dump())
    db.add(review)
    db.commit()
    db.refresh(review)
    _refresh_track_rating(db, payload.track_id)
    db.refresh(review)
    return review


@router.get("/reviews", response_model=list[ReviewRead], tags=["Reviews"])
def list_reviews(
    track_id: int | None = Query(default=None, description="Filter reviews by track ID"),
    reviewer_name: str | None = Query(default=None, description="Filter by reviewer name (partial match)"),
    min_rating: int | None = Query(default=None, ge=1, le=5, description="Minimum rating filter"),
    limit: int = Query(default=20, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(default=0, ge=0, description="Number of results to skip"),
    db: Session = Depends(get_db),
):
    """List reviews with optional filtering and pagination."""
    query = db.query(Review)
    if track_id is not None:
        query = query.filter(Review.track_id == track_id)
    if reviewer_name:
        query = query.filter(Review.reviewer_name.ilike(f"%{reviewer_name}%"))
    if min_rating is not None:
        query = query.filter(Review.rating >= min_rating)
    return query.order_by(Review.created_at.desc()).offset(offset).limit(limit).all()


@router.get("/reviews/{review_id}", response_model=ReviewRead, tags=["Reviews"])
def get_review(review_id: int, db: Session = Depends(get_db)):
    """Return a single review by its ID."""
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.put("/reviews/{review_id}", response_model=ReviewRead, tags=["Reviews"])
def update_review(review_id: int, payload: ReviewUpdate, db: Session = Depends(get_db)):
    """Update an existing review (partial update supported)."""
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    for field, value in payload.model_dump(exclude_none=True).items():
        setattr(review, field, value)

    db.add(review)
    db.commit()
    db.refresh(review)
    _refresh_track_rating(db, review.track_id)
    db.refresh(review)
    return review


@router.delete("/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Reviews"])
def delete_review(review_id: int, db: Session = Depends(get_db)):
    """Delete a review by its ID."""
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    track_id = review.track_id
    db.delete(review)
    db.commit()
    _refresh_track_rating(db, track_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------

@router.post("/tags", response_model=UserTagRead, status_code=status.HTTP_201_CREATED, tags=["Tags"])
def create_tag(payload: UserTagCreate, db: Session = Depends(get_db)):
    """Create a user tag for a track."""
    track = db.query(Track).filter(Track.id == payload.track_id).first()
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    existing = (
        db.query(UserTag)
        .filter(UserTag.track_id == payload.track_id, UserTag.tag_name == payload.tag_name)
        .first()
    )
    if existing:
        raise HTTPException(status_code=409, detail="Tag already exists for this track")

    tag = UserTag(**payload.model_dump())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.get("/tags", response_model=list[UserTagRead], tags=["Tags"])
def list_tags(
    track_id: int | None = Query(default=None, description="Filter tags by track ID"),
    db: Session = Depends(get_db),
):
    """List user tags with optional track filtering."""
    query = db.query(UserTag)
    if track_id is not None:
        query = query.filter(UserTag.track_id == track_id)
    return query.order_by(UserTag.created_at.desc()).all()


@router.delete("/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tags"])
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    """Delete a user tag by its ID."""
    tag = db.query(UserTag).filter(UserTag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------------------------
# Collections
# ---------------------------------------------------------------------------

@router.post("/collections", response_model=CollectionRead, status_code=status.HTTP_201_CREATED, tags=["Collections"])
def create_collection(payload: CollectionCreate, db: Session = Depends(get_db)):
    """Create a new track collection."""
    existing = db.query(Collection).filter(Collection.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="Collection name already exists")
    collection = Collection(**payload.model_dump())
    db.add(collection)
    db.commit()
    db.refresh(collection)
    return collection


@router.get("/collections", response_model=list[CollectionRead], tags=["Collections"])
def list_collections(db: Session = Depends(get_db)):
    """Return all collections ordered by creation date."""
    return db.query(Collection).order_by(Collection.created_at.desc()).all()


@router.get("/collections/{collection_id}", tags=["Collections"])
def get_collection(collection_id: int, db: Session = Depends(get_db)):
    """Return a collection with its track items."""
    collection = db.query(Collection).filter(Collection.id == collection_id).first()
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    items = (
        db.query(CollectionItem, Track, Genre)
        .join(Track, CollectionItem.track_id == Track.id)
        .join(Genre, Track.genre_id == Genre.id)
        .filter(CollectionItem.collection_id == collection_id)
        .order_by(Track.title.asc())
        .all()
    )

    return {
        "id": collection.id,
        "name": collection.name,
        "description": collection.description,
        "created_by": collection.created_by,
        "created_at": collection.created_at,
        "item_count": len(items),
        "items": [
            {
                "item_id": item.id,
                "note": item.note,
                "track": {
                    "id": track.id,
                    "title": track.title,
                    "artist_name": track.artist_name,
                    "album_title": track.album_title,
                    "genre_name": genre.name,
                    "average_rating": track.average_rating,
                },
            }
            for item, track, genre in items
        ],
    }


@router.post("/collections/{collection_id}/items", status_code=status.HTTP_201_CREATED, tags=["Collections"])
def add_track_to_collection(
    collection_id: int,
    payload: CollectionItemCreate,
    db: Session = Depends(get_db),
):
    """Add a track to an existing collection."""
    collection = db.query(Collection).filter(Collection.id == collection_id).first()
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    track = db.query(Track).filter(Track.id == payload.track_id).first()
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    existing = (
        db.query(CollectionItem)
        .filter(
            CollectionItem.collection_id == collection_id,
            CollectionItem.track_id == payload.track_id,
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=409, detail="Track already exists in this collection")

    item = CollectionItem(collection_id=collection_id, **payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return {
        "message": "Track added to collection",
        "collection_id": collection_id,
        "track_id": payload.track_id,
        "item_id": item.id,
    }


@router.delete("/collections/{collection_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Collections"])
def delete_collection(collection_id: int, db: Session = Depends(get_db)):
    """Delete a collection and all its items."""
    collection = db.query(Collection).filter(Collection.id == collection_id).first()
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    db.query(CollectionItem).filter(CollectionItem.collection_id == collection_id).delete()
    db.delete(collection)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete(
    "/collections/{collection_id}/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Collections"],
)
def remove_item_from_collection(
    collection_id: int,
    item_id: int,
    db: Session = Depends(get_db),
):
    """Remove a track item from a collection."""
    item = (
        db.query(CollectionItem)
        .filter(
            CollectionItem.id == item_id,
            CollectionItem.collection_id == collection_id,
        )
        .first()
    )
    if not item:
        raise HTTPException(status_code=404, detail="Collection item not found")
    db.delete(item)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------

@router.get("/analytics/top-rated-tracks", tags=["Analytics"])
def top_rated_tracks(
    limit: int = Query(default=5, ge=1, le=20, description="Number of top tracks to return"),
    db: Session = Depends(get_db),
):
    """Return the highest-rated tracks that have at least one review."""
    rows = (
        db.query(
            Track.id,
            Track.title,
            Track.artist_name,
            Genre.name.label("genre_name"),
            Track.average_rating,
            func.count(Review.id).label("review_count"),
        )
        .join(Genre, Track.genre_id == Genre.id)
        .outerjoin(Review, Review.track_id == Track.id)
        .group_by(Track.id, Genre.name)
        .having(func.count(Review.id) > 0)
        .order_by(
            Track.average_rating.desc(),
            func.count(Review.id).desc(),
            Track.title.asc(),
        )
        .limit(limit)
        .all()
    )
    return [dict(row._mapping) for row in rows]


@router.get("/analytics/genre-summary", tags=["Analytics"])
def genre_summary(db: Session = Depends(get_db)):
    """Return a summary of each genre including track count and average rating."""
    rows = (
        db.query(
            Genre.name.label("genre_name"),
            func.count(Track.id).label("track_count"),
            func.round(func.avg(Track.average_rating), 2).label("average_track_rating"),
        )
        .outerjoin(Track, Track.genre_id == Genre.id)
        .group_by(Genre.id)
        .order_by(Genre.name.asc())
        .all()
    )
    return [dict(row._mapping) for row in rows]


@router.get("/analytics/top-tags", tags=["Analytics"])
def top_tags(
    limit: int = Query(default=10, ge=1, le=50, description="Number of top tags to return"),
    db: Session = Depends(get_db),
):
    """Return the most frequently used tags across all tracks."""
    rows = (
        db.query(UserTag.tag_name, func.count(UserTag.id).label("usage_count"))
        .group_by(UserTag.tag_name)
        .order_by(func.count(UserTag.id).desc(), UserTag.tag_name.asc())
        .limit(limit)
        .all()
    )
    return [dict(row._mapping) for row in rows]


@router.get("/analytics/mood-distribution", tags=["Analytics"])
def mood_distribution(db: Session = Depends(get_db)):
    """Return the distribution of moods across all tracks."""
    rows = (
        db.query(
            Track.mood,
            func.count(Track.id).label("track_count"),
        )
        .filter(Track.mood.isnot(None))
        .group_by(Track.mood)
        .order_by(func.count(Track.id).desc(), Track.mood.asc())
        .all()
    )
    return [dict(row._mapping) for row in rows]


@router.get("/analytics/review-activity", tags=["Analytics"])
def review_activity(db: Session = Depends(get_db)):
    """Return overall review activity summary and per-reviewer breakdown."""
    total_reviews = db.query(func.count(Review.id)).scalar() or 0
    average_rating = db.query(func.round(func.avg(Review.rating), 2)).scalar()

    rows = (
        db.query(
            Review.reviewer_name,
            func.count(Review.id).label("review_count"),
            func.round(func.avg(Review.rating), 2).label("average_rating"),
        )
        .group_by(Review.reviewer_name)
        .order_by(func.count(Review.id).desc())
        .all()
    )
    return {
        "total_reviews": total_reviews,
        "average_rating": float(average_rating) if average_rating is not None else 0.0,
        "reviewers": [dict(row._mapping) for row in rows],
    }
