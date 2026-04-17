# Presentation Script and Q&A Preparation
**Course:** XJCO3011 - Web Services and Web Data
**Project:** Music Appreciation and Discovery API
**Target Duration:** 5 Minutes (Approx. 650-750 words)

## Presentation Script

### Slide 1: Title Slide (0:00 - 0:30)
"Good morning, everyone. My name is [Your Name], and today I will be presenting my coursework project for XJCO3011: the Music Appreciation and Discovery API. This project is a fully functional, database-backed RESTful web service that allows users to explore music, manage track collections, and share their listening experiences. As you can see on the screen, the system currently features 25 API endpoints, is backed by 55 automated tests, and has been successfully deployed live on PythonAnywhere."

### Slide 2: Problem & Solution (0:30 - 1:00)
"The core problem this API addresses is the lack of a structured backend for music enthusiasts to catalogue their listening experiences and tag tracks by mood in a unified ecosystem. My solution is a comprehensive RESTful API that supports structured browsing, full CRUD operations for reviews, user-defined tagging, and analytical insights. Throughout development, my design philosophy was deliberate scope control—prioritising stability, testability, and explainability over unnecessary complexity."

### Slide 3: Architecture & Technology Stack (1:00 - 1:30)
"To achieve this, I selected a modern, robust technology stack. I used FastAPI for the routing layer because of its excellent performance and automatic OpenAPI documentation generation. For data access, I implemented SQLAlchemy 2.0, which allowed me to build powerful aggregation queries without writing raw SQL. The database is SQLite, chosen specifically because it is zero-configuration and highly examiner-friendly. To ensure data integrity, Pydantic handles strict payload validation, and API key authentication protects all write operations."

### Slide 4: Database Design (1:30 - 2:00)
"The underlying data model consists of six core entities with well-defined relationships. At the centre is the 'Track' entity, which belongs to a 'Genre' and can have multiple 'Reviews' and 'UserTags'. Users can also group tracks into 'Collections' via the 'CollectionItem' linking table. This relational structure is what makes the rich querying and analytics possible."

### Slide 5: API Endpoints Overview (2:00 - 2:30)
"The API surface area is extensive but logically organised into 7 groups, totalling 25 endpoints. We have general health checks, read-only endpoints for Genres and Tracks, and full CRUD endpoints for Reviews, Tags, and Collections. Importantly, I implemented a clear security boundary: all read operations are public, while all write operations—POST, PUT, and DELETE—require a valid API key passed via the X-API-Key header."

### Slide 6: CRUD Demo: Reviews (2:30 - 3:00)
"Let's look at the Review lifecycle as an example of the CRUD functionality. When a user POSTs a new review, they must provide their API key. They can then GET reviews using filters like track ID or minimum rating, with offset-based pagination built in. If they PUT an update or DELETE a review, the system automatically triggers a background recalculation of the track's average rating, ensuring data consistency at all times."

### Slide 7: Analytics Endpoints (3:00 - 3:30)
"To elevate the project beyond basic CRUD, I implemented 5 dedicated analytics endpoints. These endpoints leverage advanced SQLAlchemy features like `func.avg`, `func.count`, `outerjoin`, and `group_by`. For instance, the system can return the top-rated tracks, summarize track counts and average ratings per genre, or analyze the distribution of moods across the entire catalogue."

### Slide 8: Testing & Quality Assurance (3:30 - 4:00)
"Reliability was a major focus of this project. I developed a comprehensive test suite using pytest and FastAPI's TestClient. The suite contains 55 automated tests spread across 9 test classes, covering everything from basic routing to complex validation edge cases and authentication failures. I'm pleased to report that all 55 tests pass consistently in under one second."

### Slide 9: Version Control & Deliverables (4:00 - 4:30)
"Throughout development, I maintained a consistent commit history on GitHub, demonstrating incremental progress. The project is fully documented, with a 5-page Technical Report, comprehensive API documentation, and a detailed README. Furthermore, the API is not just a local prototype; it is actively deployed and accessible live on PythonAnywhere."

### Slide 10: Conclusion & Future Work (4:30 - 5:00)
"In conclusion, this project successfully delivers a clean, modular, and fully tested web service that meets all coursework requirements. While the current implementation uses a single shared API key and SQLite, future work could involve migrating to PostgreSQL, implementing OAuth2 for per-user authentication, and integrating with external APIs like Spotify to enrich the track catalogue. Thank you for listening, and I am happy to take any questions."

---

## Anticipated Q&A

### 1. Why did you choose FastAPI over Flask or Django?
**Answer:** "I chose FastAPI primarily for its speed, its native support for asynchronous programming, and its automatic generation of OpenAPI documentation (Swagger UI). Unlike Flask, which requires external extensions for robust API building, FastAPI has Pydantic validation and serialization built right in. Compared to Django, FastAPI is much lighter and more modular, which fit perfectly with my design philosophy of deliberate scope control."

### 2. How does your automatic rating recalculation work?
**Answer:** "I implemented a helper function called `_refresh_track_rating`. Whenever a review is created, updated, or deleted, this function is called. It uses SQLAlchemy's `func.avg` to calculate the new average rating for all reviews associated with that specific `track_id`, and then updates the `average_rating` field on the Track model. This ensures that the track's rating is always perfectly synchronized with its underlying reviews."

### 3. You mentioned API Key authentication. Why not OAuth2 or JWT?
**Answer:** "For this coursework prototype, I wanted to establish a clear boundary between public read operations and protected write operations without overcomplicating the setup for the examiners. A single shared API key achieves this goal effectively. Implementing full OAuth2 with JWT would require user registration, password hashing, and token management endpoints, which fell outside the focused scope of this coursework. However, the dependency injection system in FastAPI makes it very easy to swap the API key dependency for an OAuth2 dependency in the future."

### 4. How did you ensure your tests are isolated from one another?
**Answer:** "I used pytest fixtures. Specifically, I created a `session`-scoped fixture that yields a FastAPI `TestClient`. Within this fixture, I use FastAPI's `Lifespan` manager, which automatically drops all existing tables, creates fresh tables, and injects the seed data before the test session begins. Additionally, for tests that create unique resources like Collections, I used Python's `uuid` module to append random strings to the names, preventing unique constraint violations across different tests."

### 5. Why did you use SQLite instead of a more robust database like PostgreSQL?
**Answer:** "SQLite was chosen specifically for its zero-configuration nature. Because it is a file-based database, the examiners can clone my repository and run the API immediately without needing to install or configure a separate database server. While it lacks the concurrency support needed for a high-traffic production environment, it is perfectly suited for a coursework prototype. Since I used SQLAlchemy ORM, migrating to PostgreSQL in the future would simply require changing the connection string and installing the `psycopg2` driver."
