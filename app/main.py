"""Music Appreciation and Discovery API — application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, SessionLocal, engine
from app.errors import register_error_handlers
from app.models import Collection, CollectionItem, Genre, Review, Track, UserTag
from app.routers.api import router as api_router
from app.seed import seed_initial_data


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Create tables and seed data on startup; clean up on shutdown."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_initial_data(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="Music Appreciation and Discovery API",
    description=(
        "A coursework API for track exploration, reviews, tags, "
        "collections, and simple analytics. Built with FastAPI, "
        "SQLAlchemy, and SQLite. Write operations require an API key "
        "via the X-API-Key header."
    ),
    version="0.3.0",
    lifespan=lifespan,
)

# Register structured error handlers
register_error_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["General"])
def root() -> dict:
    """Return a welcome message with links to documentation."""
    return {
        "message": "Music Appreciation and Discovery API is running.",
        "docs": "/docs",
        "redoc": "/redoc",
        "version": "0.3.0",
        "authentication": "Write operations require X-API-Key header.",
    }


@app.get("/health", tags=["General"])
def health() -> dict:
    """Return a simple health-check response."""
    return {"status": "ok"}


app.include_router(api_router)
