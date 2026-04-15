# API Plan

## Project Goal

The API will support a coursework scenario focused on **music appreciation and discovery**. The system will store music metadata and allow users to record their appreciation through reviews, custom tags, and collections. It will also expose lightweight analytics endpoints that make the project more than a basic CRUD implementation.

## Data Model Scope

| Entity | Purpose | Notes |
|---|---|---|
| Genre | Store music genre information | Supports summaries and filtering |
| Track | Store track-level metadata | Seeded from a starter dataset |
| Review | Main CRUD entity | Required coursework focus |
| UserTag | Store custom appreciation tags | Adds user interpretation layer |
| Collection | Store named personal collections | Represents playlists or themed lists |
| CollectionItem | Link tracks to collections | Resolves many-to-many relation |

## Planned Relationships

| Relationship | Description |
|---|---|
| Genre 1-to-many Track | One genre can contain many tracks |
| Track 1-to-many Review | One track can have many reviews |
| Track 1-to-many UserTag | One track can have many user tags |
| Collection many-to-many Track | Implemented via CollectionItem |

## Minimum Endpoint Scope

### General

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Root message |
| GET | `/health` | Service health check |

### Tracks and Genres

| Method | Path | Purpose |
|---|---|---|
| GET | `/tracks` | List tracks with optional filtering |
| GET | `/tracks/{track_id}` | Retrieve a single track |
| GET | `/genres` | List genres |

### Reviews

| Method | Path | Purpose |
|---|---|---|
| POST | `/reviews` | Create review |
| GET | `/reviews` | List reviews |
| GET | `/reviews/{review_id}` | Retrieve a single review |
| PUT | `/reviews/{review_id}` | Update review |
| DELETE | `/reviews/{review_id}` | Delete review |

### Tags and Collections

| Method | Path | Purpose |
|---|---|---|
| POST | `/tags` | Create a user tag |
| DELETE | `/tags/{tag_id}` | Delete a user tag |
| POST | `/collections` | Create a collection |
| GET | `/collections` | List collections |
| POST | `/collections/{collection_id}/items` | Add a track to a collection |

### Analytics

| Method | Path | Purpose |
|---|---|---|
| GET | `/analytics/top-rated-tracks` | Tracks with highest average rating |
| GET | `/analytics/genre-summary` | Track counts and average ratings by genre |
| GET | `/analytics/top-tags` | Most frequent user tags |

## Development Strategy

The implementation should follow a stable incremental path:

| Step | Goal |
|---|---|
| 1 | Build models and database session |
| 2 | Implement track and genre read endpoints |
| 3 | Implement review CRUD |
| 4 | Add tags and collections |
| 5 | Add analytics |
| 6 | Add tests and seed data |
| 7 | Refine documentation and handover materials |

## Scope Control Rule

This coursework project should avoid unnecessary complexity. The first complete version does not require:

- advanced authentication;
- external API integrations;
- recommendation algorithms;
- audio playback;
- cloud infrastructure.

These may be mentioned as future work instead.
