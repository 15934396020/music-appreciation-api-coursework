# Music Appreciation and Discovery API

## Project Overview

This project is a coursework API for **music appreciation and discovery**. It is designed as a data-driven web service that supports track browsing, genre browsing, review CRUD, user tags, personal collections, and simple analytics. The implementation strategy intentionally prioritises clarity, stability, and explainability so that the project can achieve a solid middle-to-upper coursework outcome.

## Coursework Positioning

The project is designed to satisfy the module requirement of a database-backed API with CRUD functionality and additional analytical value. Instead of focusing on audio playback or advanced machine learning, it focuses on music metadata and user-generated appreciation data, which is more realistic to implement, easier to justify, and easier to present in an oral examination.

## Planned Features

| Area | Scope |
|---|---|
| Core data | Tracks and genres |
| CRUD focus | Reviews |
| User interaction | Tags and collections |
| Analytics | Top-rated tracks, genre summaries, top tags, collection insights |
| Documentation | Swagger UI plus coursework-oriented Markdown/PDF deliverables |

## Technical Stack

| Layer | Choice |
|---|---|
| Backend framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Testing | Pytest / smoke tests |
| Version control | Git + GitHub |

## Current Repository Structure

```text
music-appreciation-api/
├── app/
├── data/
├── docs/
├── handover/
├── scripts/
├── tests/
└── requirements.txt
```

## Run Instructions

After dependencies are installed, the app can be started with:

```bash
uvicorn app.main:app --reload
```

The API documentation will then be available at:

```text
http://127.0.0.1:8000/docs
```

## Multi-Account Collaboration Rule

This repository is intentionally structured for continuation across multiple sessions. Every new session must read the files inside `handover/` before changing code, and every ending session must update those files before stopping.

Start with the following order:

1. `handover/README.md`
2. 2. `handover/CURRENT_STATUS.md`
   3. 3. `handover/NEXT_ACTIONS.md`
      4. 4. `handover/SESSION_LOG.md`
         5. 5. `docs/API_PLAN.md`
           
            6. ## Current Status
           
            7. The repository structure and handover protocol have been created. The FastAPI skeleton has also been started. Models, routers, test coverage, and seed data are still under implementation.
            8. 
