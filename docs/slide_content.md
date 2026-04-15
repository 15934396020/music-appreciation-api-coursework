# Music Appreciation and Discovery API — Presentation Slides

## Slide 1: Music Appreciation and Discovery API
**Heading:** A FastAPI-Powered Music Exploration Service with CRUD, Tags, Collections, and Analytics

This presentation introduces the Music Appreciation and Discovery API, developed for the XJCO3011 Web Services and Web Data module. The project delivers a fully functional, database-backed RESTful API that enables users to explore music metadata, write reviews, assign interpretive tags, build themed collections, and retrieve analytical insights. Built with FastAPI, SQLAlchemy, and SQLite, the system prioritises clarity, stability, and explainability.

- Module: XJCO3011 — Web Services and Web Data
- Project type: Individual API Development Coursework
- Core technology: FastAPI + SQLAlchemy + SQLite
- Key deliverables: Working API, 48 automated tests, full documentation

---

## Slide 2: Music Appreciation Needs a Structured Backend
**Heading:** Music listeners interpret tracks personally — but simple catalogues fail to capture that richness

Music enthusiasts do more than just listen: they rate, tag, categorise, and curate tracks into meaningful collections. Existing music platforms focus on streaming and recommendation algorithms, but rarely expose structured APIs for user-generated appreciation data. This project addresses that gap by providing a backend service where every interaction — from writing a review to building a themed playlist — is captured as structured, queryable data.

- Problem: No lightweight API exists for structured music appreciation data
- Opportunity: Reviews, tags, and collections represent rich user-generated content
- Solution: A RESTful API that makes appreciation data first-class citizens
- Approach: Focus on metadata and user interaction, not audio streaming

---

## Slide 3: Deliberately Scoped for Coursework Quality
**Heading:** Strategic scope control ensures a coherent, fully testable system

The project was deliberately scoped to deliver a complete, polished system rather than an ambitious but incomplete one. Core features include track and genre browsing, full review CRUD, user tags, collections, and five analytics endpoints. Authentication, audio playback, and external API dependencies were intentionally excluded to maintain focus and ensure every feature is thoroughly tested and documented.

| In Scope | Out of Scope |
|---|---|
| 25 tracks across 8 genres | Audio playback |
| Full review CRUD with validation | User authentication |
| Tags and collections management | Recommendation engine |
| 5 analytics endpoints | External API integration |
| 48 automated tests | Cloud deployment |

---

## Slide 4: Clean Multi-Tier Architecture Powers the API
**Heading:** Client requests flow through four well-separated layers to SQLite

The system follows a standard multi-tier architecture. HTTP requests are routed by FastAPI, validated by Pydantic schemas, processed through SQLAlchemy ORM queries, and persisted in a SQLite database. This separation of concerns ensures that each layer can be tested, modified, or replaced independently. The application uses FastAPI's modern lifespan context manager for database initialization and seed data injection on startup.

- **Routing Layer:** FastAPI handles 25 endpoint definitions across 7 groups
- **Validation Layer:** Pydantic enforces rating ranges (1-5), string lengths, and required fields
- **Data Access Layer:** SQLAlchemy ORM manages complex joins and aggregations
- **Database:** SQLite provides zero-configuration persistence with 25 seeded tracks

---

## Slide 5: Six Core Entities Model the Music Appreciation Domain
**Heading:** Genre, Track, Review, UserTag, Collection, and CollectionItem form a coherent relational schema

The database schema centres on the Track entity, which connects to Genre (many-to-one), Review (one-to-many), UserTag (one-to-many), and CollectionItem (many-to-many via Collection). This design supports rich querying: for example, the analytics endpoints can aggregate ratings by genre, count tags across tracks, and summarise reviewer activity — all through standard SQL joins and group-by operations.

| Entity | Role | Key Fields |
|---|---|---|
| Genre | Classifies tracks into 8 categories | name, description |
| Track | Central music metadata entity | title, artist, mood, play_count, average_rating |
| Review | Main CRUD resource (1-5 rating) | reviewer_name, rating, comment |
| UserTag | User-defined descriptive labels | tag_name, created_by |
| Collection | Themed grouping of tracks | name, description, created_by |
| CollectionItem | Links tracks to collections | track_id, collection_id, note |

---

## Slide 6: 25 Endpoints Deliver Complete API Functionality
**Heading:** Seven endpoint groups cover browsing, CRUD, curation, and analytics

The API exposes 25 endpoints organised into seven logical groups. The Reviews group implements full CRUD with automatic average rating recalculation. Tracks support filtering by title, artist, genre, and mood, with offset-based pagination. Collections allow users to create themed playlists and manage their contents. The Analytics group provides five aggregation endpoints that go beyond basic CRUD to deliver real analytical value.

| Group | Endpoints | Highlights |
|---|---|---|
| General | 2 | Health check, welcome message |
| Genres | 2 | List all, get by ID |
| Tracks | 2 | List with 4 filters + pagination, get by ID |
| Reviews | 5 | Full CRUD + filtering by track, reviewer, min rating |
| Tags | 3 | Create, list (filter by track), delete |
| Collections | 6 | Create, list, detail with items, add/remove items, delete |
| Analytics | 5 | Top-rated, genre summary, top tags, mood distribution, review activity |

---

## Slide 7: Live Demonstration Walkthrough
**Heading:** A realistic user journey from browsing tracks to viewing analytics

The demonstration follows a natural user workflow: first browsing the track catalogue, then interacting with specific tracks through reviews and tags, building a personal collection, and finally viewing analytical summaries. Each step is executed through the Swagger UI interface, showing real HTTP requests and JSON responses.

1. Open Swagger UI at `/docs` — show auto-generated interactive documentation
2. `GET /tracks?genre=Jazz` — filter the catalogue by genre
3. `GET /tracks/6` — retrieve detailed information for "Take Five"
4. `POST /reviews` — create a 5-star review with comment
5. `PUT /reviews/{id}` — update the review rating to 4
6. `POST /tags` — tag the track as "iconic"
7. `POST /collections` + `POST /collections/{id}/items` — create "Jazz Favourites" collection
8. `GET /analytics/genre-summary` — view aggregated genre statistics

---

## Slide 8: Analytics Endpoints Elevate the Project Beyond Basic CRUD
**Heading:** Five aggregation endpoints transform raw data into actionable insights

The analytics module demonstrates advanced SQLAlchemy querying capabilities including `func.avg`, `func.count`, `group_by`, `outerjoin`, and `having` clauses. These endpoints provide immediate value for potential dashboard clients and demonstrate a deeper understanding of relational data processing than basic CRUD alone.

| Endpoint | What It Returns |
|---|---|
| `/analytics/top-rated-tracks` | Highest-rated tracks with review counts (requires at least 1 review) |
| `/analytics/genre-summary` | Track count and average rating per genre |
| `/analytics/top-tags` | Most frequently used tags across all tracks |
| `/analytics/mood-distribution` | Distribution of mood keywords across the catalogue |
| `/analytics/review-activity` | Total reviews, average rating, and per-reviewer breakdown |

---

## Slide 9: 48 Automated Tests Confirm System Reliability
**Heading:** Comprehensive pytest suite covers all endpoints, edge cases, and validation rules

The test suite contains 48 automated tests organised into 7 test classes, covering every endpoint group plus dedicated validation edge cases. Tests use FastAPI's TestClient with a session-scoped fixture that properly triggers the lifespan context manager, ensuring database tables are created and seed data is injected before any test runs. All 48 tests pass consistently.

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

## Slide 10: Strengths, Limitations, and Future Directions
**Heading:** A coherent, well-tested prototype with clear paths for enhancement

The project successfully delivers a complete, well-documented API with 25 endpoints, 48 passing tests, and comprehensive documentation. The deliberate scope control ensured every feature was fully implemented and tested rather than partially built. Key limitations include the absence of user authentication and reliance on static seed data. Future work could add OAuth2 authentication, PostgreSQL migration, external API integration (Spotify/MusicBrainz), and a frontend client.

**Strengths:** Complete CRUD, rich analytics, 48 tests, modern FastAPI patterns, full documentation

**Limitations:** No authentication, SQLite only, static seed data

**Future Work:** OAuth2 tokens, PostgreSQL migration, Spotify/MusicBrainz integration, React frontend
