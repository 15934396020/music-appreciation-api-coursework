# Design and Implementation of a Music Appreciation and Discovery API

**Module:** XJCO3011 - Web Services and Web Data  
**Project:** Coursework 1 - Individual Web Services API Development Project  
**GitHub Repository:** [music-appreciation-api-coursework](https://github.com/15934396020/music-appreciation-api-coursework)  
**Live Deployment:** https://weidademiaoxiao.pythonanywhere.com  
**API Documentation:** See `docs/API_DOCUMENTATION.pdf` in the repository  

---

## 1. Introduction

This technical report details the design, implementation, and evaluation of the **Music Appreciation and Discovery API**, developed as part of the XJCO3011 coursework. The primary aim of this project is to build a robust, database-backed RESTful web service that allows users to explore music metadata and generate interpretive content.

Rather than focusing on complex audio streaming or machine learning recommendation engines, this project deliberately targets music metadata and user-generated appreciation data (reviews, tags, and collections). This scope ensures a clear, stable, and explainable system architecture that fully satisfies the module's requirement for CRUD functionality while adding analytical value through data aggregation.

## 2. Problem Definition and Project Scope

Music enthusiasts often need a structured way to catalogue their listening experiences, group tracks by mood or genre, and share reviews. The Music Appreciation and Discovery API solves this by providing a backend service where users can:

- Browse a curated catalogue of 29 tracks across 8 genres.
- Create, read, update, and delete (CRUD) track reviews.
- Assign descriptive tags to tracks.
- Build and manage personal track collections.
- Retrieve analytical summaries (e.g., top-rated tracks, genre statistics, mood distributions).

**Out of Scope:** Audio playback and external API integration (e.g., Spotify/Last.fm) were excluded to maintain a focused, coursework-appropriate prototype, though the architecture is designed to accommodate these in the future.

## 3. Requirements Analysis

The system was designed to meet the following requirements:

### 3.1 Functional Requirements

- **Core Data Retrieval:** List and filter tracks by title, artist, genre, and mood with pagination support.
- **Review Management:** Full CRUD operations for user reviews, including automatic recalculation of a track's average rating.
- **User Interaction:** Endpoints to create and delete user tags, and to manage track collections (create collection, add/remove items, delete collection).
- **Analytics:** Aggregation endpoints to provide insights such as top-rated tracks, genre summaries, mood distributions, and review activity.
- **Authentication:** API key-based authentication for all write operations, while read operations remain publicly accessible.

### 3.2 Non-Functional Requirements

- **Simplicity and Maintainability:** Clean, modular code structure with separated concerns (routing, validation, data access, authentication).
- **Reliability:** Comprehensive error handling with structured JSON error responses and input validation.
- **Testability:** High test coverage using automated test suites (55 tests across 9 test classes).
- **Documentation:** Auto-generated interactive API documentation (Swagger UI) and static PDF documentation.
- **Deployment:** Externally hosted ASGI deployment on PythonAnywhere, accessible at `https://weidademiaoxiao.pythonanywhere.com`.

## 4. System Design

The system follows a standard multi-tier web architecture:

1. **Client Layer:** HTTP requests (tested via `httpx` and Swagger UI).
2. **Authentication Layer:** API key validation via the `X-API-Key` header for write operations.
3. **Routing Layer (FastAPI):** Handles HTTP routing, parameter parsing, and response formatting.
4. **Validation Layer (Pydantic):** Ensures incoming payloads meet strict data type and length constraints.
5. **Data Access Layer (SQLAlchemy ORM):** Maps Python objects to database tables and handles complex queries (e.g., joins and aggregations).
6. **Database (SQLite):** A lightweight, file-based relational database ideal for prototyping.

### 4.1 Data Model

The core entities and their relationships are:

- **Genre:** One-to-many relationship with Tracks. Contains name and description.
- **Track:** The central entity. Has one Genre, many Reviews, many UserTags, and can belong to many Collections via CollectionItems. Stores a denormalised `average_rating` field that is automatically recalculated.
- **Review:** Belongs to one Track. Contains rating (1-5), comment text, and timestamps.
- **UserTag:** Belongs to one Track. Represents a user-defined descriptor with a unique constraint on (track_id, tag_name).
- **Collection & CollectionItem:** A Collection contains many CollectionItems, each linking to a specific Track with an optional note. A unique constraint prevents duplicate tracks within a collection.

## 5. Implementation Details

### 5.1 Technology Stack Justification

- **FastAPI (0.115.12):** Chosen for its high performance, modern Python type hints, and automatic OpenAPI documentation generation. Its `lifespan` context manager provides a clean way to handle database initialisation and data seeding on startup.
- **SQLAlchemy (2.0.40):** Selected as the ORM for its powerful querying capabilities, which were essential for building the analytics endpoints without writing raw SQL.
- **Pydantic (2.11.3):** Used for robust request payload validation (e.g., enforcing review ratings between 1 and 5, and string length limits).
- **SQLite:** Chosen for its zero-configuration setup, making the repository easily runnable by examiners without requiring a separate database server installation.

### 5.2 Authentication Implementation

The API implements a lightweight API key authentication scheme using FastAPI's dependency injection system. The design follows a deliberate split between read and write operations:

- **Public endpoints (GET):** All read operations remain publicly accessible without authentication, allowing unrestricted browsing of tracks, genres, reviews, tags, collections, and analytics.
- **Protected endpoints (POST, PUT, DELETE):** All write operations require a valid API key passed via the `X-API-Key` header.

The authentication module (`app/auth.py`) uses FastAPI's `Security` dependency with `APIKeyHeader` to extract and validate the key. Invalid or missing keys return structured JSON error responses with appropriate HTTP status codes (401 for missing keys, 403 for invalid keys). This approach was chosen over more complex OAuth2/JWT implementations because it provides meaningful access control while remaining simple enough for coursework demonstration and examiner testing.

### 5.3 Structured Error Handling

A custom error handling module (`app/errors.py`) registers exception handlers for both HTTP exceptions and Pydantic validation errors. All error responses follow a consistent JSON structure:

```json
{
    "error": "validation_error",
    "message": "Request validation failed.",
    "details": [{"field": "body -> rating", "message": "...", "type": "..."}]
}
```

This ensures that API consumers receive predictable, machine-readable error responses regardless of the error type.

### 5.4 Key Implementation Features

- **Lifespan Management:** The application uses FastAPI's modern `@asynccontextmanager` lifespan event to automatically create database tables and inject 29 seed tracks across 8 genres upon startup.
- **Dynamic Rating Calculation:** When a review is created, updated, or deleted, a helper function `_refresh_track_rating` automatically recalculates the track's average rating using SQL aggregation, ensuring data consistency.
- **Pagination and Filtering:** The `/tracks` and `/reviews` endpoints implement offset-based pagination and multiple query filters (e.g., partial string matching using `ilike`).
- **CORS Middleware:** Cross-Origin Resource Sharing is enabled to allow frontend applications to interact with the API.

## 6. Analytics and Added Value

To elevate the project beyond basic CRUD operations, a dedicated `/analytics` router was implemented. These endpoints leverage SQLAlchemy's `func.count`, `func.avg`, `group_by`, and `outerjoin` features to provide:

- **Top-Rated Tracks:** Ranks tracks based on average rating and review volume, filtering out unreviewed tracks using `having`.
- **Genre Summary:** Calculates the total number of tracks and the average rating per genre.
- **Top Tags:** Returns the most frequently used tags across all tracks.
- **Mood Distribution:** Aggregates tracks by their assigned mood.
- **Review Activity:** Summarises the total number of reviews and average ratings submitted by individual reviewers.

These features demonstrate a deeper understanding of relational data querying and provide immediate value to potential frontend dashboard clients.

## 7. Testing and Evaluation

A comprehensive automated test suite was developed using `pytest` and FastAPI's `TestClient`.

- **Test Coverage:** The suite contains **55 tests** across **9 test classes** covering all endpoint groups (General, Genres, Tracks, Reviews, Tags, Collections, Analytics, Authentication, and Validation).
- **Test Isolation:** A custom `pytest.fixture` with `scope="session"` ensures the FastAPI lifespan event is triggered correctly during testing, initialising the database and seed data once for the entire test session.
- **Authentication Testing:** Dedicated tests verify that write operations return 401 without an API key and 403 with an invalid key, while confirming that all GET endpoints remain publicly accessible.
- **Validation Testing:** Edge cases, such as submitting a review with a rating of 6 or an empty collection name, are explicitly tested to ensure the API returns the correct `422 Unprocessable Entity` status with structured error details.

All 55 tests currently pass, confirming the system's stability and adherence to the defined requirements.

## 8. Limitations and Future Work

While the current implementation successfully meets the coursework objectives, several limitations exist:

1. **Single API Key:** The current authentication uses a single shared API key rather than per-user credentials. Implementing OAuth2 with JWT tokens would enable user-specific resource ownership and access control.
2. **Database Scalability:** SQLite is excellent for prototyping but lacks the concurrency support needed for a production environment. Migrating to PostgreSQL or MySQL would be a logical next step.
3. **External Integrations:** The API relies on static seed data. Integrating with external APIs like Spotify or MusicBrainz could dynamically enrich the track catalogue.
4. **Rate Limiting:** No request rate limiting is currently implemented. Adding rate limiting would protect the API from abuse in a production setting.

## 9. Conclusion

The Music Appreciation and Discovery API successfully demonstrates the design and implementation of a modern, database-backed web service. By leveraging FastAPI and SQLAlchemy, the project delivers a clean, modular, externally hosted, and fully tested RESTful API with 25 endpoints, API key authentication, structured error handling, and 5 analytical query endpoints. The live deployment at `https://weidademiaoxiao.pythonanywhere.com` strengthens the coursework submission by showing that the system is not only functional in local development but also accessible on an external web server. The inclusion of comprehensive testing (55 automated tests) and robust input validation ensures the system is resilient, explainable, and well aligned with the criteria for the XJCO3011 coursework.

---

## GenAI Declaration

In accordance with the module's GREEN GenAI policy, generative AI tools (specifically Manus AI / LLMs) were utilised integrally throughout this project.

**Purposes of GenAI Usage:**

- **Architecture Design:** Exploring alternative API frameworks (Flask vs FastAPI vs Django REST) and evaluating trade-offs for the coursework context.
- **Code Generation & Refactoring:** Assisting in the migration from deprecated `on_event("startup")` to modern FastAPI `lifespan` handlers, implementing the authentication module, and creating the structured error handling system.
- **Data Generation:** Creating the comprehensive seed dataset of 29 tracks and 8 genres with realistic metadata.
- **Test Suite Development:** Generating edge-case validation tests, authentication tests, and resolving session-scope fixture configurations in `pytest`.
- **Documentation:** Drafting the Markdown and LaTeX API documentation, structuring this technical report, and creating presentation materials.
- **Multi-Account Collaboration:** Establishing a handover protocol that enables seamless project continuation across multiple AI sessions.

The use of GenAI significantly accelerated the development process, allowing for a greater focus on architectural design, data relationships, and analytical query logic. All AI-generated code was thoroughly reviewed, tested, and manually refined to ensure correctness and alignment with the project goals. Conversation logs are available in `docs/GENAI_CONVERSATION_LOG.md`.
