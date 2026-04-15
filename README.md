# Music Appreciation and Discovery API

## Project Overview

This project is a coursework API for **music appreciation and discovery**, built as part of the XJCO3011 Designing and Building User Interfaces module. It provides a data-driven web service that supports track browsing, genre exploration, review management (full CRUD), user-generated tags, personal collections, and analytical endpoints. The implementation prioritises clarity, stability, and explainability.

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
│   ├── conftest.py           # Shared test fixtures
│   └── test_api.py           # 48 comprehensive test cases
├── docs/                     # Technical report and API documentation
├── handover/                 # Cross-session handover documents
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

The API will be available at `http://127.0.0.1:8000`. Interactive documentation is served at:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Running Tests

```bash
pytest -q
```

All 48 tests should pass, covering general endpoints, genre and track browsing, review CRUD, tags, collections, analytics, and input validation.

## API Endpoints Overview

| Method | Path | Description |
|---|---|---|
| GET | `/` | Welcome message and links |
| GET | `/health` | Health check |
| GET | `/genres` | List all genres |
| GET | `/genres/{id}` | Get genre by ID |
| GET | `/tracks` | List tracks (with filtering, sorting, pagination) |
| GET | `/tracks/{id}` | Get track by ID |
| POST | `/reviews` | Create a review |
| GET | `/reviews` | List reviews (with filtering) |
| GET | `/reviews/{id}` | Get review by ID |
| PUT | `/reviews/{id}` | Update a review |
| DELETE | `/reviews/{id}` | Delete a review |
| POST | `/tags` | Create a tag |
| GET | `/tags` | List tags |
| DELETE | `/tags/{id}` | Delete a tag |
| POST | `/collections` | Create a collection |
| GET | `/collections` | List collections |
| GET | `/collections/{id}` | Get collection with items |
| POST | `/collections/{id}/items` | Add track to collection |
| DELETE | `/collections/{id}` | Delete a collection |
| DELETE | `/collections/{id}/items/{item_id}` | Remove item from collection |
| GET | `/analytics/top-rated-tracks` | Top-rated tracks |
| GET | `/analytics/genre-summary` | Genre statistics |
| GET | `/analytics/top-tags` | Most-used tags |
| GET | `/analytics/mood-distribution` | Mood distribution |
| GET | `/analytics/review-activity` | Review activity summary |

## Multi-Account Collaboration

This repository is structured for continuation across multiple sessions. Every new session must read the files inside `handover/` before changing code, and every ending session must update those files before stopping. Start with:

1. `handover/FOR_NEXT_ACCOUNT.md`
2. `handover/CURRENT_STATUS.md`
3. `handover/NEXT_ACTIONS.md`
4. `handover/SESSION_LOG.md`

## Licence

This project is submitted as coursework for XJCO3011 at the University of Leeds. All rights reserved.
