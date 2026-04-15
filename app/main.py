from fastapi import FastAPI

from app.database import Base, SessionLocal, engine
from app.models import Collection, CollectionItem, Genre, Review, Track, UserTag
from app.routers.api import router as api_router
from app.seed import seed_initial_data

app = FastAPI(
    title="Music Appreciation and Discovery API",
    description="A coursework API for track exploration, reviews, tags, collections, and simple analytics.",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_initial_data(db)
    finally:
        db.close()


@app.get("/")
def root() -> dict:
    return {
        "message": "Music Appreciation and Discovery API is running.",
        "docs": "/docs",
        "version": "0.1.0",
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


app.include_router(api_router)
