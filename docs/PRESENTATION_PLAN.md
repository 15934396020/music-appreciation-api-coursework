# Presentation Plan

## Purpose

This document defines the recommended structure for the coursework presentation. The goal is to make the oral presentation concise, confident, and easy to follow without promising a level of complexity that the project was never meant to deliver.

## Recommended Presentation Positioning

The presentation should frame the project as a **well-scoped, database-backed music appreciation API** that combines CRUD functionality with light analytics and clear documentation.

> The strongest presentation angle is not “this project does everything”, but rather “this project was designed carefully, implemented coherently, and can be explained clearly.”

## Recommended Slide Sequence

| Slide | Purpose |
|---|---|
| 1. Title and overview | Introduce the project name and its coursework goal |
| 2. Problem and motivation | Explain why music appreciation is a suitable and interesting API domain |
| 3. Project scope | Show what the API does and what is intentionally out of scope |
| 4. System architecture | Present the main technical stack and component flow |
| 5. Database design | Explain the core entities and their relationships |
| 6. API design | Summarise endpoint groups and CRUD focus |
| 7. Demonstration flow | Walk through a realistic usage path |
| 8. Analytics features | Show the extra value beyond basic CRUD |
| 9. Testing and validation | Demonstrate evidence of correctness |
| 10. Reflection and future work | Conclude with strengths, limitations, and realistic extensions |

## Slide-by-Slide Notes

### Slide 1. Title and Overview

This slide should contain the project title, your name, module code, and a one-sentence summary such as:

> A FastAPI-based music appreciation API supporting track exploration, review CRUD, tags, collections, and analytics.

### Slide 2. Problem and Motivation

This slide should explain that music listeners often interpret tracks in different personal and thematic ways, but simple song catalogues do not capture those appreciation-oriented interactions. The API therefore combines structured metadata with user-generated interpretation.

### Slide 3. Project Scope

A compact scope table is useful.

| In scope | Out of scope |
|---|---|
| Track browsing | Audio playback |
| Genre browsing | Advanced recommendation engine |
| Review CRUD | Authentication system |
| User tags | External API dependency in core version |
| Collections | Full frontend application |
| Analytics | Cloud-scale deployment |

### Slide 4. System Architecture

This slide should show a simple architecture chain:

| Layer | Technology |
|---|---|
| API layer | FastAPI |
| Validation | Pydantic |
| ORM | SQLAlchemy |
| Database | SQLite |
| Testing | Pytest |

A diagram can be added later for visual clarity.

### Slide 5. Database Design

This slide should highlight the core data entities.

| Entity | Role |
|---|---|
| Genre | Classifies tracks |
| Track | Stores music metadata |
| Review | Main CRUD entity |
| UserTag | Captures user interpretation |
| Collection | Groups tracks into themes |
| CollectionItem | Links tracks to collections |

### Slide 6. API Design

This slide should group endpoints clearly.

| Endpoint group | Purpose |
|---|---|
| General | Health and root endpoints |
| Tracks and genres | Browsing and retrieval |
| Reviews | Core CRUD |
| Tags | User-generated descriptors |
| Collections | Themed grouping of tracks |
| Analytics | Summary and insight endpoints |

### Slide 7. Demonstration Flow

This slide should outline the live or narrated demo sequence.

| Step | Demo action |
|---|---|
| 1 | Open Swagger UI |
| 2 | Show `GET /tracks` |
| 3 | Show `GET /tracks/{id}` |
| 4 | Create a review with `POST /reviews` |
| 5 | Update or delete a review |
| 6 | Add a tag |
| 7 | Create a collection and add a track |
| 8 | Show analytics endpoint output |

### Slide 8. Analytics Features

This slide should emphasise that the project goes beyond minimum CRUD through endpoints such as top-rated tracks, genre summaries, and top tags.

### Slide 9. Testing and Validation

This slide should mention the evidence already available.

| Validation type | Evidence |
|---|---|
| Automated tests | Current pytest suite passes |
| Manual checks | Key routes were verified locally |
| Data correctness | Ratings update track averages |
| API usability | Swagger documentation available through FastAPI |

### Slide 10. Reflection and Future Work

This final slide should stress that the current version is intentionally coherent and realistic. It should then mention a few controlled future extensions such as authentication, richer datasets, and optional external metadata integration.

## Recommended Speaking Strategy

The presentation should sound deliberate and calm. The speaker should repeatedly connect design decisions to coursework constraints, explaining not only what was built, but **why this level of scope was the right choice**.

## Current Materials Already Available

| Material | Location |
|---|---|
| Core implementation | `app/` |
| Test evidence | `tests/test_api.py` |
| API structure | `docs/API_PLAN.md` |
| Setup and project overview | `README.md` |
| Multi-session history | `handover/` |

## Next Presentation Step

The next session can turn this plan into actual slide content or a slide deck, using about 8 to 10 slides depending on the coursework time limit.
