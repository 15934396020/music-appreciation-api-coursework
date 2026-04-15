# Music Appreciation and Discovery API Documentation

## Overview

The Music Appreciation and Discovery API is a RESTful web service designed to facilitate the exploration of music tracks, genres, and user-generated content such as reviews, tags, and collections. It provides a robust set of endpoints for data retrieval, CRUD operations, and analytical insights.

This document outlines the available endpoints, their parameters, and expected responses.

## Base URL

All endpoints are relative to the base URL of the application. In a local development environment, this is typically:

```text
http://127.0.0.1:8000
```

## Authentication

Currently, the API does not require authentication. All endpoints are publicly accessible for demonstration and coursework evaluation purposes.

## Endpoints

### 1. General

#### `GET /`
Returns a welcome message and links to the interactive documentation.
- **Response (200 OK):**
  ```json
  {
    "message": "Music Appreciation and Discovery API is running.",
    "docs": "/docs",
    "redoc": "/redoc",
    "version": "0.2.0"
  }
  ```

#### `GET /health`
Returns a simple health-check response to verify the API is operational.
- **Response (200 OK):**
  ```json
  {
    "status": "ok"
  }
  ```

---

### 2. Genres

#### `GET /genres`
Retrieves a list of all available music genres, ordered alphabetically.
- **Response (200 OK):** Array of Genre objects.
  ```json
  [
    {
      "id": 1,
      "name": "Ambient",
      "description": "Atmospheric and meditative soundscapes designed for deep listening and relaxation."
    }
  ]
  ```

#### `GET /genres/{genre_id}`
Retrieves a specific genre by its ID.
- **Parameters:**
  - `genre_id` (path, integer): The ID of the genre.
- **Response (200 OK):** Genre object.
- **Response (404 Not Found):** If the genre does not exist.

---

### 3. Tracks

#### `GET /tracks`
Retrieves a list of tracks with optional filtering, sorting, and pagination.
- **Query Parameters:**
  - `title` (string, optional): Filter by track title (partial match).
  - `artist` (string, optional): Filter by artist name (partial match).
  - `genre` (string, optional): Filter by genre name (partial match).
  - `mood` (string, optional): Filter by mood keyword (partial match).
  - `sort_by` (string, default="title"): Sort field (`title`, `artist`, `rating`, `play_count`).
  - `order` (string, default="asc"): Sort order (`asc` or `desc`).
  - `limit` (integer, default=20, max=100): Maximum number of results to return.
  - `offset` (integer, default=0): Number of results to skip.
- **Response (200 OK):** Array of Track objects.

#### `GET /tracks/{track_id}`
Retrieves a specific track by its ID.
- **Parameters:**
  - `track_id` (path, integer): The ID of the track.
- **Response (200 OK):** Track object including nested genre details.
- **Response (404 Not Found):** If the track does not exist.

---

### 4. Reviews

#### `POST /reviews`
Creates a new review for a track.
- **Request Body:**
  ```json
  {
    "track_id": 1,
    "reviewer_name": "John Doe",
    "rating": 5,
    "comment": "An absolute masterpiece."
  }
  ```
- **Response (201 Created):** The created Review object.
- **Response (404 Not Found):** If the specified track does not exist.
- **Response (422 Unprocessable Entity):** If validation fails (e.g., rating not between 1 and 5).

#### `GET /reviews`
Retrieves a list of reviews with optional filtering and pagination.
- **Query Parameters:**
  - `track_id` (integer, optional): Filter reviews by track ID.
  - `reviewer_name` (string, optional): Filter by reviewer name (partial match).
  - `min_rating` (integer, optional): Minimum rating filter (1-5).
  - `limit` (integer, default=20, max=100): Maximum number of results.
  - `offset` (integer, default=0): Number of results to skip.
- **Response (200 OK):** Array of Review objects.

#### `GET /reviews/{review_id}`
Retrieves a specific review by its ID.
- **Parameters:**
  - `review_id` (path, integer): The ID of the review.
- **Response (200 OK):** Review object.
- **Response (404 Not Found):** If the review does not exist.

#### `PUT /reviews/{review_id}`
Updates an existing review. Supports partial updates.
- **Parameters:**
  - `review_id` (path, integer): The ID of the review.
- **Request Body:** (All fields optional)
  ```json
  {
    "rating": 4,
    "comment": "Updated comment text."
  }
  ```
- **Response (200 OK):** The updated Review object.
- **Response (404 Not Found):** If the review does not exist.

#### `DELETE /reviews/{review_id}`
Deletes a review by its ID.
- **Parameters:**
  - `review_id` (path, integer): The ID of the review.
- **Response (204 No Content):** Successful deletion.
- **Response (404 Not Found):** If the review does not exist.

---

### 5. Tags

#### `POST /tags`
Creates a new user tag for a track.
- **Request Body:**
  ```json
  {
    "track_id": 1,
    "tag_name": "masterpiece",
    "created_by": "Jane Doe"
  }
  ```
- **Response (201 Created):** The created Tag object.
- **Response (404 Not Found):** If the track does not exist.
- **Response (409 Conflict):** If the tag already exists for this track.

#### `GET /tags`
Retrieves a list of user tags, optionally filtered by track.
- **Query Parameters:**
  - `track_id` (integer, optional): Filter tags by track ID.
- **Response (200 OK):** Array of Tag objects.

#### `DELETE /tags/{tag_id}`
Deletes a user tag by its ID.
- **Parameters:**
  - `tag_id` (path, integer): The ID of the tag.
- **Response (204 No Content):** Successful deletion.
- **Response (404 Not Found):** If the tag does not exist.

---

### 6. Collections

#### `POST /collections`
Creates a new track collection.
- **Request Body:**
  ```json
  {
    "name": "Late Night Study",
    "description": "Calm tracks for focused work.",
    "created_by": "Alice"
  }
  ```
- **Response (201 Created):** The created Collection object.
- **Response (409 Conflict):** If a collection with the same name already exists.

#### `GET /collections`
Retrieves a list of all collections, ordered by creation date.
- **Response (200 OK):** Array of Collection objects.

#### `GET /collections/{collection_id}`
Retrieves a specific collection along with its track items.
- **Parameters:**
  - `collection_id` (path, integer): The ID of the collection.
- **Response (200 OK):** Collection object including an array of `items`.
- **Response (404 Not Found):** If the collection does not exist.

#### `POST /collections/{collection_id}/items`
Adds a track to an existing collection.
- **Parameters:**
  - `collection_id` (path, integer): The ID of the collection.
- **Request Body:**
  ```json
  {
    "track_id": 1,
    "note": "Great opening track."
  }
  ```
- **Response (201 Created):** Confirmation message and item details.
- **Response (404 Not Found):** If the collection or track does not exist.
- **Response (409 Conflict):** If the track is already in the collection.

#### `DELETE /collections/{collection_id}`
Deletes a collection and all its items.
- **Parameters:**
  - `collection_id` (path, integer): The ID of the collection.
- **Response (204 No Content):** Successful deletion.
- **Response (404 Not Found):** If the collection does not exist.

#### `DELETE /collections/{collection_id}/items/{item_id}`
Removes a specific track item from a collection.
- **Parameters:**
  - `collection_id` (path, integer): The ID of the collection.
  - `item_id` (path, integer): The ID of the collection item.
- **Response (204 No Content):** Successful deletion.
- **Response (404 Not Found):** If the collection item does not exist.

---

### 7. Analytics

#### `GET /analytics/top-rated-tracks`
Returns the highest-rated tracks that have at least one review.
- **Query Parameters:**
  - `limit` (integer, default=5, max=20): Number of top tracks to return.
- **Response (200 OK):** Array of track summary objects.

#### `GET /analytics/genre-summary`
Returns a summary of each genre, including track count and average rating.
- **Response (200 OK):** Array of genre summary objects.

#### `GET /analytics/top-tags`
Returns the most frequently used tags across all tracks.
- **Query Parameters:**
  - `limit` (integer, default=10, max=50): Number of top tags to return.
- **Response (200 OK):** Array of tag summary objects.

#### `GET /analytics/mood-distribution`
Returns the distribution of moods across all tracks.
- **Response (200 OK):** Array of mood summary objects.

#### `GET /analytics/review-activity`
Returns overall review activity summary and per-reviewer breakdown.
- **Response (200 OK):** Object containing `total_reviews`, `average_rating`, and an array of `reviewers`.

## Data Models

### Track
```json
{
  "id": 1,
  "title": "Clair de Lune",
  "artist_name": "Claude Debussy",
  "album_title": "Suite bergamasque",
  "duration_seconds": 300,
  "mood": "dreamy",
  "play_count": 1500,
  "average_rating": 4.5,
  "genre": {
    "id": 1,
    "name": "Classical",
    "description": "..."
  }
}
```

### Review
```json
{
  "id": 1,
  "track_id": 1,
  "reviewer_name": "John Doe",
  "rating": 5,
  "comment": "An absolute masterpiece.",
  "created_at": "2023-10-27T10:00:00Z",
  "updated_at": "2023-10-27T10:00:00Z"
}
```
