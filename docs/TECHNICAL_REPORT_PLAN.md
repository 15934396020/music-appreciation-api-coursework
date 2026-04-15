# Technical Report Plan

## Purpose

This document defines the recommended structure for the coursework technical report. It is intentionally aligned with the current implementation strategy so that later writing can be completed efficiently without changing the project direction.

## Recommended Report Title

**Design and Implementation of a Music Appreciation and Discovery API Using FastAPI and SQLite**

## Recommended Report Structure

| Section | What it should contain |
|---|---|
| 1. Introduction | Brief context of the coursework, motivation for choosing music appreciation, and report aim |
| 2. Problem Definition and Project Scope | What the API is designed to solve, what user actions it supports, and scope boundaries |
| 3. Requirements Analysis | Functional requirements, non-functional requirements, and success criteria |
| 4. System Design | Architecture, database schema, key entities, and endpoint groups |
| 5. Implementation | Stack, main modules, CRUD logic, validation, seed data, and testing |
| 6. Analytics and Added Value | How the analytics endpoints improve the system beyond basic CRUD |
| 7. Testing and Evaluation | Smoke tests, manual endpoint verification, and discussion of system behaviour |
| 8. Limitations and Future Work | Current scope limits and realistic future enhancements |
| 9. Conclusion | Overall reflection on whether the project goals were achieved |

## Suggested Writing Angle

The report should repeatedly communicate one key idea:

> The project was deliberately designed to be **clear, stable, and explainable**, with enough breadth to demonstrate database-backed API design, while remaining realistic for coursework delivery.

## Section-by-Section Notes

### 1. Introduction

This section should explain that the project explores music appreciation through metadata and user-generated interpretation rather than audio streaming. That makes it technically manageable and academically appropriate for a CRUD-focused API project.

### 2. Problem Definition and Project Scope

This section should clarify that users need a way to browse tracks, group music by genre, record reviews, assign interpretive tags, build themed collections, and retrieve simple analytical summaries. It should also state what is out of scope, such as authentication, recommendation engines, and audio playback.

### 3. Requirements Analysis

A clear table is recommended.

| Requirement Type | Suggested items |
|---|---|
| Functional | Track listing, track detail, review CRUD, tag creation, collection management, analytics |
| Non-functional | Simplicity, maintainability, testability, explainability, Git-based version control |

### 4. System Design

This section should include:

| Design element | What to show |
|---|---|
| Architecture summary | Client → FastAPI → SQLAlchemy → SQLite |
| Data model | Genre, Track, Review, UserTag, Collection, CollectionItem |
| Relationship explanation | One-to-many and many-to-many relations |
| Endpoint grouping | General, tracks, reviews, tags, collections, analytics |

A diagram may later be added to improve clarity.

### 5. Implementation

This section should describe the following in prose and tables:

| Subtopic | Suggested explanation |
|---|---|
| Framework choice | Why FastAPI was chosen for clear API development and built-in docs |
| ORM choice | Why SQLAlchemy supports maintainable models and relationships |
| Database | Why SQLite is suitable for a coursework prototype |
| Seed data | Why a compact starter dataset was used |
| Validation | Pydantic schemas and rating constraints |
| CRUD | Review lifecycle from create to delete |

### 6. Analytics and Added Value

This section should highlight that the project goes beyond minimal CRUD by adding summary endpoints such as top-rated tracks, genre-level summaries, and top tags. This helps position the project above a bare minimum implementation while keeping complexity under control.

### 7. Testing and Evaluation

This section should mention both automated and manual checks.

| Test area | Current evidence |
|---|---|
| Health check | Verified via endpoint response |
| Track retrieval | Verified manually and by test client |
| Review CRUD | Verified by automated test |
| Tag and collection flow | Verified by automated test |
| Analytics | Verified by automated test |

### 8. Limitations and Future Work

Suitable future work includes:

| Area | Future extension |
|---|---|
| Authentication | Add user accounts and protected personal collections |
| External metadata | Integrate MusicBrainz or Last.fm in a later version |
| Recommendation support | Add rule-based or data-driven discovery features |
| UI | Add a simple frontend client |

### 9. Conclusion

This section should argue that the coursework goals were met through a coherent API system with a clear domain model, working CRUD functionality, useful analytics, reproducible setup, and maintainable project structure.

## Current Evidence Already Available in Repository

| Evidence | Location |
|---|---|
| Core code | `app/` |
| Tests | `tests/test_api.py` |
| API scope | `docs/API_PLAN.md` |
| Collaboration history | `handover/` |
| Setup instructions | `README.md` |

## Next Writing Step

The next session can convert this plan into a real report draft section by section, starting with the introduction, requirements analysis, and system design.
