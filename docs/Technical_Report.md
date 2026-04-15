# Design and Implementation of a Music Appreciation and Discovery API Using FastAPI and SQLite

**Coursework:** XJCO3011 Designing and Building User Interfaces
**Author:** Manus AI
**Date:** April 2026

---

## 1. Introduction

This report details the design, implementation, and evaluation of the **Music Appreciation and Discovery API**, developed as coursework for the XJCO3011 module. The project explores music appreciation through metadata and user-generated interpretation rather than audio streaming. This approach makes the project technically manageable and academically appropriate for a database-backed API project, focusing on data relationships, CRUD operations, and analytical value. The project was deliberately designed to be clear, stable, and explainable, with enough breadth to demonstrate robust API design while remaining realistic for coursework delivery.

## 2. Problem Definition and Project Scope

Music enthusiasts often need a structured way to organise their listening experiences, categorise tracks, and discover new music based on community feedback. The API is designed to solve this by providing a platform where users can:
- Browse tracks and group music by genre.
- Record and manage reviews with ratings and comments.
- Assign interpretive tags to tracks.
- Build themed personal collections.
- Retrieve analytical summaries (e.g., top-rated tracks, mood distributions).

**Out of Scope:** To maintain a focused and achievable coursework scope, features such as user authentication, advanced recommendation engines, and actual audio playback are excluded.

## 3. Requirements Analysis

The system requirements are divided into functional and non-functional categories to ensure a comprehensive and reliable API.

### Functional Requirements
| Requirement | Description |
|---|---|
| **Track & Genre Browsing** | Users can list, filter, sort, and retrieve details for tracks and genres. |
| **Review Management** | Full CRUD (Create, Read, Update, Delete) operations for track reviews. |
| **Tagging System** | Users can create and delete custom tags for tracks. |
| **Collections** | Users can create collections, add/remove tracks, and delete collections. |
| **Analytics** | Endpoints to retrieve top-rated tracks, genre summaries, top tags, and review activity. |

### Non-functional Requirements
| Requirement | Description |
|---|---|
| **Simplicity & Clarity** | Code must be easy to read, understand, and explain during assessment. |
| **Maintainability** | Clear separation of concerns (routers, models, schemas). |
| **Testability** | High test coverage ensuring reliability of all endpoints. |
| **Documentation** | Auto-generated interactive API documentation (Swagger UI/ReDoc). |

## 4. System Design

The system follows a standard modern web architecture: **Client → FastAPI → SQLAlchemy → SQLite**.

### Data Model
The database schema consists of six core entities:
1. **Genre**: Represents musical categories (e.g., Classical, Jazz).
2. **Track**: Represents individual songs, linked to a Genre (Many-to-One).
3. **Review**: User reviews for tracks, including ratings and comments (Many-to-One with Track).
4. **UserTag**: Custom descriptive tags assigned to tracks (Many-to-One with Track).
5. **Collection**: User-created playlists or groupings.
6. **CollectionItem**: The association table linking Tracks to Collections (Many-to-Many).

### Endpoint Architecture
Endpoints are logically grouped using FastAPI routers:
- `/genres` and `/tracks`: Core data retrieval and filtering.
- `/reviews`: Primary CRUD resource.
- `/tags` and `/collections`: User interaction and curation.
- `/analytics`: Aggregated data insights.

## 5. Implementation

The implementation leverages a modern Python stack chosen for performance, developer experience, and coursework suitability.

| Component | Technology | Justification |
|---|---|---|
| **Framework** | FastAPI (0.115.12) | High performance, automatic OpenAPI documentation, and clear routing. |
| **Database** | SQLite | Zero-configuration, file-based database ideal for prototypes and coursework. |
| **ORM** | SQLAlchemy (2.0.40) | Robust handling of complex relationships and SQL generation. |
| **Validation** | Pydantic (2.11.3) | Strict request/response schema validation and type hinting. |

### Key Implementation Details
- **Lifespan Management**: The application uses FastAPI's modern `lifespan` context manager to automatically create database tables and inject seed data (29 tracks across 8 genres) upon startup.
- **Validation**: Pydantic models enforce strict rules, such as review ratings being between 1 and 5, and comment lengths being constrained.
- **Dynamic Updates**: When a review is created, updated, or deleted, a helper function `_refresh_track_rating` automatically recalculates and updates the track's average rating.

## 6. Analytics and Added Value

To elevate the project beyond a basic CRUD application, several analytical endpoints were implemented using SQLAlchemy's aggregation functions (`func.count`, `func.avg`):
- **Top-Rated Tracks**: Returns tracks ordered by average rating and review count.
- **Genre Summary**: Provides track counts and average ratings grouped by genre.
- **Mood Distribution**: Shows the frequency of different moods across the track database.
- **Review Activity**: Summarises total reviews, overall average rating, and activity per reviewer.

These endpoints demonstrate the ability to write complex SQL queries via an ORM and provide immediate value to potential API consumers.

## 7. Testing and Evaluation

The system's reliability is ensured through a comprehensive automated test suite using `pytest` and FastAPI's `TestClient`.

- **Test Coverage**: 48 automated tests cover all endpoint groups.
- **Test Areas**:
  - **General**: Health checks and root endpoint verification.
  - **Browsing**: Pagination, filtering (by title, artist, genre, mood), and sorting logic.
  - **CRUD Operations**: Full lifecycle testing for reviews, tags, and collections, including edge cases (e.g., deleting non-existent items).
  - **Validation**: Ensuring the API correctly rejects invalid inputs (e.g., out-of-range ratings, empty names) with HTTP 422 errors.
  - **Analytics**: Verifying aggregation logic and response structures.

All 48 tests pass successfully, confirming that the system behaves exactly as specified in the requirements.

## 8. Limitations and Future Work

While the current implementation successfully meets the coursework requirements, several areas could be expanded in future iterations:

| Area | Potential Enhancement |
|---|---|
| **Authentication** | Implement OAuth2 with JWT to support user accounts and secure personal collections. |
| **External APIs** | Integrate with external services like MusicBrainz or Spotify API to automatically fetch rich track metadata and album art. |
| **Recommendation** | Develop a basic recommendation engine based on user tags and review history. |
| **Frontend UI** | Build a React or Vue.js frontend to consume the API and provide a graphical user interface. |

## 9. Conclusion

The Music Appreciation and Discovery API successfully fulfills the coursework objectives. By focusing on a clear domain model, implementing robust CRUD functionality with strict validation, and adding valuable analytical endpoints, the project demonstrates a solid understanding of backend API design. The use of FastAPI and SQLAlchemy resulted in a maintainable, well-documented, and fully tested system (48 passing tests) that serves as a strong foundation for future development. The project's emphasis on clarity and stability ensures it is well-prepared for assessment and oral examination.
