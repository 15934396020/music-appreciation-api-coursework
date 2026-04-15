# Music Appreciation and Discovery API — Presentation Slides

## Metadata
- **Topic**: Music Appreciation and Discovery API — Design, Implementation, and Evaluation
- **Audience**: Academic assessors (XJCO3011 module, University of Leeds)
- **Tone**: Professional, clear, and technically grounded
- **Visual style**: Clean, modern, with dark blue and white colour scheme. Use code snippets and architecture diagrams where appropriate.

---

## Slide 1: Title Slide
**Heading**: Music Appreciation and Discovery API
**Subheading**: XJCO3011 Designing and Building User Interfaces — Coursework Presentation

This presentation introduces the Music Appreciation and Discovery API, developed for the XJCO3011 module. The project delivers a fully functional, database-backed RESTful API that enables users to explore music metadata, write reviews, assign interpretive tags, build themed collections, and retrieve analytical insights. Built with FastAPI, SQLAlchemy, and SQLite, the system prioritises clarity, stability, and explainability.

- Module: XJCO3011 — Designing and Building User Interfaces
- Project type: Individual API Development Coursework
- Core technology: FastAPI + SQLAlchemy + SQLite
- Key deliverables: Working API, 48 automated tests, full documentation

---

## Slide 2: Music listeners need structured tools to capture their appreciation
**Heading**: Music listeners interpret tracks personally — but simple catalogues fail to capture that richness

Music enthusiasts do more than just listen: they rate, tag, categorise, and curate tracks into meaningful collections. This project addresses the gap by providing a backend service where every interaction — from writing a review to building a themed playlist — is captured as structured, queryable data. The approach focuses on metadata and user-generated interpretation rather than audio streaming.

- Problem: No lightweight API exists for structured music appreciation data
- Opportunity: Reviews, tags, and collections represent rich user-generated content
- Solution: A RESTful API that makes appreciation data first-class citizens
- Approach: Focus on metadata and user interaction, not audio streaming

---

## Slide 3: Strategic scope control ensures a coherent, fully testable system
**Heading**: Deliberately scoped for coursework quality — complete rather than ambitious

The project was deliberately scoped to deliver a complete, polished system rather than an ambitious but incomplete one. Core features include track and genre browsing, full review CRUD, user tags, collections, and five analytics endpoints. Authentication, audio playback, and external API dependencies were intentionally excluded to maintain focus.

| In Scope | Out of Scope |
|---|---|
| 29 tracks across 8 genres | Audio playback |
| Full review CRUD with validation | User authentication |
| Tags and collections management | Recommendation engine |
| 5 analytics endpoints | External API integration |
| 48 automated tests | Cloud deployment |

---

## Slide 4: A clean multi-tier architecture powers the API
**Heading**: Client requests flow through four well-separated layers to SQLite

The system follows a standard multi-tier architecture. HTTP requests are routed by FastAPI, validated by Pydantic schemas, processed through SQLAlchemy ORM queries, and persisted in a SQLite database. This separation of concerns ensures that each layer can be tested, modified, or replaced independently. The application uses FastAPI's modern lifespan context manager for database initialization and seed data injection on startup.

- **Routing Layer:** FastAPI handles 25 endpoint definitions across 7 groups
- **Validation Layer:** Pydantic enforces rating ranges (1–5), string lengths, and required fields
- **Data Access Layer:** SQLAlchemy ORM manages complex joins and aggregations
- **Database:** SQLite provides zero-configuration persistence with 29 seeded tracks

| Layer | Technology | Version |
|---|---|---|
| Framework | FastAPI | 0.115.12 |
| ORM | SQLAlchemy | 2.0.40 |
| Validation | Pydantic | 2.11.3 |
| Database | SQLite | Built-in |
| Testing | Pytest + HTTPX | 8.3.5 |

---

## Slide 5: Six core entities model the music appreciation domain
**Heading**: Genre, Track, Review, UserTag, Collection, and CollectionItem form a coherent relational schema

The database schema centres on the Track entity, which connects to Genre (many-to-one), Review (one-to-many), UserTag (one-to-many), and CollectionItem (many-to-many via Collection). This design supports rich querying: analytics endpoints can aggregate ratings by genre, count tags across tracks, and summarise reviewer activity through standard SQL joins and group-by operations.

| Entity | Role | Key Fields |
|---|---|---|
| Genre | Classifies tracks into 8 categories | name, description |
| Track | Central music metadata entity | title, artist, mood, play_count, average_rating |
| Review | Main CRUD resource (1–5 rating) | reviewer_name, rating, comment |
| UserTag | User-defined descriptive labels | tag_name, created_by |
| Collection | Themed grouping of tracks | name, description, created_by |
| CollectionItem | Links tracks to collections | track_id, collection_id, note |

---

## Slide 6: 25 endpoints deliver complete API functionality
**Heading**: Seven endpoint groups cover browsing, CRUD, curation, and analytics

The API exposes 25 endpoints organised into seven logical groups. The Reviews group implements full CRUD with automatic average rating recalculation. Tracks support filtering by title, artist, genre, and mood, with offset-based pagination and sorting. Collections allow users to create themed playlists and manage their contents. The Analytics group provides five aggregation endpoints that go beyond basic CRUD.

| Group | Endpoints | Highlights |
|---|---|---|
| General | 2 | Health check, welcome message |
| Genres | 2 | List all, get by ID |
| Tracks | 2 | List with 4 filters + pagination + sorting, get by ID |
| Reviews | 5 | Full CRUD + filtering by track, reviewer, min rating |
| Tags | 3 | Create, list (filter by track), delete |
| Collections | 6 | Create, list, detail with items, add/remove items, delete |
| Analytics | 5 | Top-rated, genre summary, top tags, mood distribution, review activity |

---

## Slide 7: Review CRUD demonstrates complete lifecycle management
**Heading**: Create, read, update, and delete reviews with automatic rating recalculation

The Reviews resource is the primary CRUD entity. Creating a review validates the track exists and enforces rating (1–5) and comment constraints. Updates support partial modification. Deletion returns 204 No Content. After every create, update, or delete operation, a helper function automatically recalculates and persists the track's average rating.

1. `POST /reviews` — Create a review (validates track, enforces constraints, returns 201)
2. `GET /reviews?track_id=5&min_rating=4` — Filter reviews with pagination
3. `PUT /reviews/{id}` — Partial update (only provided fields change)
4. `DELETE /reviews/{id}` — Remove review, recalculate track average (returns 204)

---

## Slide 8: Five analytics endpoints transform raw data into actionable insights
**Heading**: Advanced SQLAlchemy aggregations elevate the project beyond basic CRUD

The analytics module demonstrates advanced querying capabilities including `func.avg`, `func.count`, `group_by`, `outerjoin`, and `having` clauses. These endpoints provide immediate value for potential dashboard clients and demonstrate a deeper understanding of relational data processing.

| Endpoint | What It Returns |
|---|---|
| `/analytics/top-rated-tracks` | Highest-rated tracks with review counts (requires at least 1 review) |
| `/analytics/genre-summary` | Track count and average rating per genre |
| `/analytics/top-tags` | Most frequently used tags across all tracks |
| `/analytics/mood-distribution` | Distribution of mood keywords across the catalogue |
| `/analytics/review-activity` | Total reviews, average rating, and per-reviewer breakdown |

---

## Slide 9: 48 automated tests confirm system reliability
**Heading**: Comprehensive pytest suite covers all endpoints, edge cases, and validation rules

The test suite contains 48 automated tests organised into 7 test classes, covering every endpoint group plus dedicated validation edge cases. Tests use FastAPI's TestClient with a session-scoped fixture that properly triggers the lifespan context manager. All 48 tests pass consistently in under 1 second.

| Test Class | Tests | Coverage |
|---|---|---|
| TestGeneralEndpoints | 2 | Root and health check |
| TestGenreEndpoints | 3 | List, get by ID, 404 handling |
| TestTrackEndpoints | 8 | Filtering, pagination, retrieval, 404 |
| TestReviewCRUD | 9 | Full lifecycle, invalid inputs, filters |
| TestTagEndpoints | 7 | Create, duplicate detection, delete |
| TestCollectionEndpoints | 9 | Create, items, duplicates, delete |
| TestAnalyticsEndpoints | 5 | All 5 analytics endpoints |
| TestValidation | 5 | Rating bounds, string lengths, limit max |

---

## Slide 10: A coherent, well-tested prototype with clear paths for enhancement
**Heading**: Strengths, limitations, and future directions

The project successfully delivers a complete, well-documented API with 25 endpoints, 48 passing tests, and comprehensive documentation. Every feature was fully implemented and tested rather than partially built.

**Strengths:** Complete CRUD, rich analytics, 48 tests, modern FastAPI patterns, full documentation

**Limitations:** No authentication, SQLite only, static seed data

**Future Work:** OAuth2 tokens, PostgreSQL migration, Spotify/MusicBrainz integration, React frontend

Thank you — questions welcome.
