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
    TrackRead,
    UserTagCreate,
    UserTagRead,
)

router = APIRouter()


def refresh_track_rating(db: Session, track_id: int) -> None:
    avg_rating = db.query(func.avg(Review.rating)).filter(Review.track_id == track_id).scalar()
    track = db.query(Track).filter(Track.id == track_id).first()
    if track:
        track.average_rating = round(float(avg_rating), 2) if avg_rating is not None else 0.0
        db.add(track)
        db.commit()


@router.get("/genres", response_model=list[GenreRead])
def list_genres(db: Session = Depends(get_db)):
    return db.query(Genre).order_by(Genre.name.asc()).all()


@router.get("/tracks", response_model=list[TrackRead])
def list_tracks(
    title: str | None = None,
    artist: str | None = None,
    genre: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(Track).options(joinedload(Track.genre))
    if title:
        query = query.filter(Track.title.ilike(f"%{title}%"))
    if artist:
        query = query.filter(Track.artist_name.ilike(f"%{artist}%"))
    if genre:
        query = query.join(Genre).filter(Genre.name.ilike(f"%{genre}%"))
    return query.order_by(Track.title.asc()).limit(limit).all()


@router.get("/tracks/{track_id}", response_model=TrackRead)
def get_track(track_id: int, db: Session = Depends(get_db)):
    track = (
        db.query(Track)
        .options(joinedload(Track.genre))
        .filter(Track.id == track_id)
        .first()
    )
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.post("/reviews", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def create_review(payload: ReviewCreate, db: Session = Depends(get_db)):
    track = db.query(Track).filter(Track.id == payload.track_id).first()
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    review = Review(**payload.model_dump())
    db.add(review)
    db.commit()
    db.refresh(review)
    refresh_track_rating(db, payload.track_id)
    db.refresh(review)
    return review


@router.get("/reviews", response_model=list[ReviewRead])
def list_reviews(track_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Review)
    if track_id is not None:
        query = query.filter(Review.track_id == track_id)
    return query.order_by(Review.created_at.desc()).all()


@router.get("/reviews/{review_id}", response_model=ReviewRead)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.put("/reviews/{review_id}", response_model=ReviewRead)
def update_review(review_id: int, payload: ReviewUpdate, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    for field, value in payload.model_dump(exclude_none=True).items():
        setattr(review, field, value)

    db.add(review)
    db.commit()
    db.refresh(review)
    refresh_track_rating(db, review.track_id)
    db.refresh(review)
    return review


@router.delete("/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    track_id = review.track_id
    db.delete(review)
    db.commit()
    refresh_track_rating(db, track_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/tags", response_model=UserTagRead, status_code=status.HTTP_201_CREATED)
def create_tag(payload: UserTagCreate, db: Session = Depends(get_db)):
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


@router.get("/tags", response_model=list[UserTagRead])
def list_tags(track_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(UserTag)
    if track_id is not None:
        query = query.filter(UserTag.track_id == track_id)
    return query.order_by(UserTag.created_at.desc()).all()


@router.delete("/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(UserTag).filter(UserTag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/collections", response_model=CollectionRead, status_code=status.HTTP_201_CREATED)
def create_collection(payload: CollectionCreate, db: Session = Depends(get_db)):
    existing = db.query(Collection).filter(Collection.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="Collection name already exists")
    collection = Collection(**payload.model_dump())
    db.add(collection)
    db.commit()
    db.refresh(collection)
    return collection


@router.get("/collections", response_model=list[CollectionRead])
def list_collections(db: Session = Depends(get_db)):
    return db.query(Collection).order_by(Collection.created_at.desc()).all()


@router.get("/collections/{collection_id}")
def get_collection(collection_id: int, db: Session = Depends(get_db)):
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


@router.post("/collections/{collection_id}/items", status_code=status.HTTP_201_CREATED)
def add_track_to_collection(collection_id: int, payload: CollectionItemCreate, db: Session = Depends(get_db)):
    collection = db.query(Collection).filter(Collection.id == collection_id).first()
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    track = db.query(Track).filter(Track.id == payload.track_id).first()
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")

    existing = (
        db.query(CollectionItem)
        .filter(CollectionItem.collection_id == collection_id, CollectionItem.track_id == payload.track_id)
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


@router.get("/analytics/top-rated-tracks")
def top_rated_tracks(limit: int = Query(default=5, ge=1, le=20), db: Session = Depends(get_db)):
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
        .order_by(Track.average_rating.desc(), func.count(Review.id).desc(), Track.title.asc())
        .limit(limit)
        .all()
    )
    return [dict(row._mapping) for row in rows]


@router.get("/analytics/genre-summary")
def genre_summary(db: Session = Depends(get_db)):
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


@router.get("/analytics/top-tags")
def top_tags(limit: int = Query(default=10, ge=1, le=20), db: Session = Depends(get_db)):
    rows = (
        db.query(UserTag.tag_name, func.count(UserTag.id).label("usage_count"))
        .group_by(UserTag.tag_name)
        .order_by(func.count(UserTag.id).desc(), UserTag.tag_name.asc())
        .limit(limit)
        .all()
    )
    return [dict(row._mapping) for row in rows]
