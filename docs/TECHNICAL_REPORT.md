# Design and Implementation of a Music Appreciation and Discovery API

**Module:** XJCO3011 - Web Services and Web Data  
**Project:** Coursework 1 - Individual Web Services API Development Project  
**Author:** Manus AI  

---

## 1. Introduction

This technical report details the design, implementation, and evaluation of the **Music Appreciation and Discovery API**, developed as part of the XJCO3011 coursework. The primary aim of this project is to build a robust, database-backed RESTful web service that allows users to explore music metadata and generate interpretive content. 

Rather than focusing on complex audio streaming or machine learning recommendation engines, this project deliberately targets music metadata and user-generated appreciation data (reviews, tags, and collections). This scope ensures a clear, stable, and explainable system architecture that fully satisfies the module's requirement for CRUD functionality while adding analytical value through data aggregation.

## 2. Problem Definition and Project Scope

Music enthusiasts often need a structured way to catalogue their listening experiences, group tracks by mood or genre, and share reviews. The Music Appreciation and Discovery API solves this by providing a backend service where users can:
- Browse a curated catalogue of tracks and genres.
- Create, read, update, and delete (CRUD) track reviews.
- Assign descriptive tags to tracks.
- Build and manage personal track collections.
- Retrieve analytical summaries (e.g., top-rated tracks, genre statistics, mood distributions).

**Out of Scope:** User authentication, audio playback, and external API integration (e.g., Spotify/Last.fm) were excluded to maintain a focused, coursework-appropriate prototype, though the architecture is designed to accommodate these in the future.

## 3. Requirements Analysis

The system was designed to meet the following requirements:

### Functional Requirements
- **Core Data Retrieval:** List and filter tracks by title, artist, genre, and mood.
- **Review Management:** Full CRUD operations for user reviews, including automatic recalculation of a track's average rating.
- **User Interaction:** Endpoints to create and delete user tags, and to manage track collections (create collection, add/remove items).
- **Analytics:** Aggregation endpoints to provide insights such as top-rated tracks, genre summaries, and review activity.

### Non-Functional Requirements
- **Simplicity and Maintainability:** Clean, modular code structure.
- **Reliability:** Comprehensive error handling and input validation.
- **Testability:** High test coverage using automated test suites.
- **Documentation:** Auto-generated interactive API documentation (Swagger UI) and static PDF documentation.

## 4. System Design

The system follows a standard multi-tier web architecture:

1. **Client Layer:** HTTP requests (tested via `httpx` and Swagger UI).
2. **Routing Layer (FastAPI):** Handles HTTP routing, parameter parsing, and response formatting.
3. **Validation Layer (Pydantic):** Ensures incoming payloads meet strict data type and length constraints.
4. **Data Access Layer (SQLAlchemy ORM):** Maps Python objects to database tables and handles complex queries (e.g., joins and aggregations).
5. **Database (SQLite):** A lightweight, file-based relational database ideal for prototyping.

### Data Model
The core entities and their relationships are:
- **Genre:** One-to-many relationship with Tracks.
- **Track:** The central entity. Has one Genre, many Reviews, many UserTags, and can belong to many Collections.
- **Review:** Belongs to one Track. Contains rating (1-5) and comment text.
- **UserTag:** Belongs to one Track. Represents a user-defined descriptor.
- **Collection & CollectionItem:** A Collection contains many CollectionItems, each linking to a specific Track.

## 5. Implementation Details

### Technology Stack Justification
- **FastAPI (0.115.12):** Chosen for its high performance, modern Python type hints, and automatic OpenAPI documentation generation. Its `lifespan` context manager provides a clean way to handle database initialization and data seeding on startup.
- **SQLAlchemy (2.0.40):** Selected as the ORM for its powerful querying capabilities, which were essential for building the analytics endpoints without writing raw SQL.
- **Pydantic (2.11.3):** Used for robust request payload validation (e.g., enforcing review ratings between 1 and 5, and string length limits).
- **SQLite:** Chosen for its zero-configuration setup, making the repository easily runnable by examiners without requiring a separate database server installation.

### Key Implementation Features
- **Lifespan Management:** The application uses FastAPI's modern `@asynccontextmanager` lifespan event to automatically create database tables and inject 25 seed tracks across 8 genres upon startup.
- **Dynamic Rating Calculation:** When a review is created, updated, or deleted, a helper function `_refresh_track_rating` automatically recalculates the track's average rating using SQL aggregation, ensuring data consistency.
- **Pagination and Filtering:** The `/tracks` and `/reviews` endpoints implement offset-based pagination and multiple query filters (e.g., partial string matching using `ilike`).

## 6. Analytics and Added Value

To elevate the project beyond basic CRUD operations, a dedicated `/analytics` router was implemented. These endpoints leverage SQLAlchemy's `func.count`, `func.avg`, `group_by`, and `outerjoin` features to provide:
- **Top-Rated Tracks:** Ranks tracks based on average rating and review volume.
- **Genre Summary:** Calculates the total number of tracks and the average rating per genre.
- **Mood Distribution:** Aggregates tracks by their assigned mood.
- **Review Activity:** Summarizes the total number of reviews and average ratings submitted by individual reviewers.

These features demonstrate a deeper understanding of relational data querying and provide immediate value to potential frontend dashboard clients.

## 7. Testing and Evaluation

A comprehensive automated test suite was developed using `pytest` and FastAPI's `TestClient`. 

- **Test Coverage:** The suite contains 48 tests covering all endpoint groups (General, Genres, Tracks, Reviews, Tags, Collections, Analytics, and Validation).
- **Test Isolation:** A custom `pytest.fixture` with `scope="session"` ensures the FastAPI lifespan event is triggered correctly during testing, initializing the in-memory database and seed data. UUIDs are used in test payloads to prevent unique constraint conflicts (e.g., duplicate collection names) across test runs.
- **Validation Testing:** Edge cases, such as submitting a review with a rating of 6 or an empty collection name, are explicitly tested to ensure the API returns the correct `422 Unprocessable Entity` status.

All 48 tests currently pass, confirming the system's stability and adherence to the defined requirements.

## 8. Limitations and Future Work

While the current implementation successfully meets the coursework objectives, several limitations exist:
1. **Lack of Authentication:** Currently, any user can delete any review or collection. Implementing OAuth2 with JWT tokens would secure user-specific resources.
2. **Database Scalability:** SQLite is excellent for prototyping but lacks the concurrency support needed for a production environment. Migrating to PostgreSQL or MySQL would be a logical next step.
3. **External Integrations:** The API relies on static seed data. Integrating with external APIs like Spotify or MusicBrainz could dynamically enrich the track catalogue.

## 9. Conclusion

The Music Appreciation and Discovery API successfully demonstrates the design and implementation of a modern, database-backed web service. By leveraging FastAPI and SQLAlchemy, the project delivers a clean, modular, and fully tested RESTful API. The inclusion of complex analytical queries and robust input validation ensures the system is not only functional but also resilient and explainable, fully satisfying the criteria for the XJCO3011 coursework.

---

## GenAI Declaration

In accordance with the module's GREEN GenAI policy, generative AI tools (specifically Manus AI / LLMs) were utilized integrally throughout this project. 

**Purposes of GenAI Usage:**
- **Code Generation & Refactoring:** Assisting in the migration from deprecated `on_event("startup")` to modern FastAPI `lifespan` handlers.
- **Data Generation:** Creating the comprehensive seed dataset of 25 tracks and 8 genres.
- **Test Suite Expansion:** Generating edge-case validation tests and resolving session-scope fixture conflicts in `pytest`.
- **Documentation:** Drafting the Markdown API documentation and structuring this technical report.

The use of GenAI significantly accelerated the development process, allowing for a greater focus on architectural design, data relationships, and analytical query logic. All AI-generated code was thoroughly reviewed, tested, and manually refined to ensure correctness and alignment with the project goals.
