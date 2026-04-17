# Music Appreciation and Discovery API

## Project Overview

This project is a coursework API for **music appreciation and discovery**, built as part of the XJCO3011 Web Services and Web Data module. It provides a data-driven web service that supports track browsing, genre exploration, review management (full CRUD), user-generated tags, personal collections, and analytical endpoints. **Write operations are protected by API key authentication**, and all errors return structured JSON responses. The implementation prioritises clarity, stability, and explainability.

## Coursework Positioning

The project satisfies the module requirement of a database-backed API with CRUD functionality and additional analytical value. Rather than focusing on audio playback or machine learning, it centres on music metadata and user-generated appreciation data — a scope that is realistic to implement, straightforward to justify, and easy to present in an oral examination.

## Features

| Area | Scope |
|---|---|
| Core data | 29 tracks across 8 genres with rich metadata |
| CRUD focus | Reviews — create, read, update, delete with validation |
| User interaction | Tags (create, list, delete) and collections (create, manage items, delete) |
| Filtering | Search tracks by title, artist, genre, mood with pagination and sorting |
| Analytics | Top-rated tracks, genre summary, top tags, mood distribution, review activity |
| Authentication | API key-based auth for write operations (X-API-Key header) |
| Error handling | Structured JSON error responses with machine-readable codes |
| Documentation | Swagger UI, ReDoc, technical report, API documentation |

## Technical Stack

| Layer | Choice | Version |
|---|---|---|
| Backend framework | FastAPI | 0.115.12 |
| Database | SQLite | Built-in |
| ORM | SQLAlchemy | 2.0.40 |
| Validation | Pydantic | 2.11.3 |
| Testing | Pytest + HTTPX | 8.3.5 / 0.28.1 |
| Server | Uvicorn | 0.34.0 |
| Version control | Git + GitHub | — |

## Repository Structure

```text
music-appreciation-api-coursework/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point with lifespan
│   ├── auth.py              # API key authentication module
│   ├── errors.py            # Structured error handling
│   ├── database.py           # SQLAlchemy engine and session setup
│   ├── seed.py               # Initial data seeding (29 tracks, 8 genres)
│   ├── models/
│   │   ├── __init__.py
│   │   └── entities.py       # SQLAlchemy ORM models
│   ├── routers/
│   │   ├── __init__.py
│   │   └── api.py            # All API endpoint definitions
│   └── schemas/
│       ├── __init__.py
│       └── entities.py       # Pydantic request/response schemas
├── tests/
│   ├── conftest.py           # Shared test fixtures (incl. auth headers)
│   └── test_api.py           # 55 comprehensive test cases
├── docs/                     # Reports, API docs, presentation, GenAI log
├── handover/                 # Cross-session handover documents
├── scripts/
│   └── create_pptx.py        # PPTX generation script
├── requirements.txt
├── pytest.ini
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.11 or later
- pip

### Installation

```bash
git clone https://github.com/15934396020/music-appreciation-api-coursework.git
cd music-appreciation-api-coursework
pip install -r requirements.txt
```

### Running the API

```bash
uvicorn app.main:app --reload
```

For local development, the API will be available at `http://127.0.0.1:8000`.

A live externally hosted deployment is also available at `https://weidademiaoxiao.pythonanywhere.com`. Interactive documentation is served at:

- **Swagger UI**: `https://weidademiaoxiao.pythonanywhere.com/docs`
- **ReDoc**: `https://weidademiaoxiao.pythonanywhere.com/redoc`

### Authentication

Write operations (POST, PUT, DELETE) require an API key via the `X-API-Key` header. Read operations (GET) are publicly accessible.

**Demo API Key:** `music-api-demo-key-2026`

```bash
# Example: Create a review (requires API key)
curl -X POST https://weidademiaoxiao.pythonanywhere.com/reviews \
  -H "Content-Type: application/json" \
  -H "X-API-Key: music-api-demo-key-2026" \
  -d '{"track_id": 1, "reviewer_name": "Alice", "rating": 5, "comment": "A masterpiece"}'
```

### Running Tests

```bash
python -m pytest -v
```

All **55 tests** across **9 test classes** should pass, covering general endpoints, genre and track browsing, review CRUD, tags, collections, analytics, authentication, and input validation.

## API Endpoints Overview

| Method | Path | Auth | Description |
|---|---|---|---|
| GET | `/` | No | Welcome message and links |
| GET | `/health` | No | Health check |
| GET | `/genres` | No | List all genres |
| GET | `/genres/{id}` | No | Get genre by ID |
| GET | `/tracks` | No | List tracks (with filtering, sorting, pagination) |
| GET | `/tracks/{id}` | No | Get track by ID |
| POST | `/reviews` | **Yes** | Create a review |
| GET | `/reviews` | No | List reviews (with filtering) |
| GET | `/reviews/{id}` | No | Get review by ID |
| PUT | `/reviews/{id}` | **Yes** | Update a review |
| DELETE | `/reviews/{id}` | **Yes** | Delete a review |
| POST | `/tags` | **Yes** | Create a tag |
| GET | `/tags` | No | List tags |
| DELETE | `/tags/{id}` | **Yes** | Delete a tag |
| POST | `/collections` | **Yes** | Create a collection |
| GET | `/collections` | No | List collections |
| GET | `/collections/{id}` | No | Get collection with items |
| POST | `/collections/{id}/items` | **Yes** | Add track to collection |
| DELETE | `/collections/{id}` | **Yes** | Delete a collection |
| DELETE | `/collections/{id}/items/{item_id}` | **Yes** | Remove item from collection |
| GET | `/analytics/top-rated-tracks` | No | Top-rated tracks |
| GET | `/analytics/genre-summary` | No | Genre statistics |
| GET | `/analytics/top-tags` | No | Most-used tags |
| GET | `/analytics/mood-distribution` | No | Mood distribution |
| GET | `/analytics/review-activity` | No | Review activity summary |

## Multi-Account Collaboration

This repository is structured for continuation across multiple sessions. Every new session must read the files inside `handover/` before changing code, and every ending session must update those files before stopping. Start with:

1. `handover/FOR_NEXT_ACCOUNT.md`
2. `handover/CURRENT_STATUS.md`
3. `handover/NEXT_ACTIONS.md`
4. `handover/SESSION_LOG.md`

## Licence

This project is submitted as coursework for XJCO3011 at the University of Leeds. All rights reserved.
