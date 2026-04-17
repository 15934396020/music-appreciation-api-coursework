"""Comprehensive test suite for the Music Appreciation and Discovery API."""

import pytest


# ---------------------------------------------------------------------------
# General endpoints
# ---------------------------------------------------------------------------

class TestGeneralEndpoints:
    """Tests for root and health endpoints."""

    def test_root_returns_welcome_message(self, test_client):
        response = test_client.get("/")
        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert "docs" in body
        assert body["version"] == "0.3.0"

    def test_health_endpoint(self, test_client):
        response = test_client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"


# ---------------------------------------------------------------------------
# Genre endpoints
# ---------------------------------------------------------------------------

class TestGenreEndpoints:
    """Tests for genre browsing."""

    def test_list_genres_returns_seeded_data(self, test_client):
        response = test_client.get("/genres")
        assert response.status_code == 200
        data = response.json()
        assert len(data) >= 5
        names = [g["name"] for g in data]
        assert "Classical" in names
        assert "Jazz" in names

    def test_get_genre_by_id(self, test_client):
        # Get the first genre from the list to use a valid ID
        genres = test_client.get("/genres").json()
        assert len(genres) > 0
        genre_id = genres[0]["id"]
        response = test_client.get(f"/genres/{genre_id}")
        assert response.status_code == 200
        assert "name" in response.json()

    def test_get_genre_not_found(self, test_client):
        response = test_client.get("/genres/9999")
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# Track endpoints
# ---------------------------------------------------------------------------

class TestTrackEndpoints:
    """Tests for track browsing and filtering."""

    def test_list_tracks_returns_seeded_data(self, test_client):
        response = test_client.get("/tracks?limit=5")
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert "title" in data[0]
        assert "genre" in data[0]

    def test_list_tracks_filter_by_title(self, test_client):
        response = test_client.get("/tracks?title=Clair")
        assert response.status_code == 200
        data = response.json()
        assert any("Clair" in t["title"] for t in data)

    def test_list_tracks_filter_by_artist(self, test_client):
        response = test_client.get("/tracks?artist=Miles")
        assert response.status_code == 200
        data = response.json()
        assert any("Miles" in t["artist_name"] for t in data)

    def test_list_tracks_filter_by_genre(self, test_client):
        response = test_client.get("/tracks?genre=Jazz")
        assert response.status_code == 200
        data = response.json()
        assert all(t["genre"]["name"] == "Jazz" for t in data)

    def test_list_tracks_filter_by_mood(self, test_client):
        response = test_client.get("/tracks?mood=calm")
        assert response.status_code == 200
        data = response.json()
        assert all("calm" in t["mood"].lower() for t in data)

    def test_list_tracks_pagination(self, test_client):
        page1 = test_client.get("/tracks?offset=0&limit=3").json()
        page2 = test_client.get("/tracks?offset=3&limit=3").json()
        assert len(page1) == 3
        assert len(page2) == 3
        assert page1[0]["id"] != page2[0]["id"]

    def test_get_track_by_id(self, test_client):
        response = test_client.get("/tracks/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "genre" in data

    def test_get_track_not_found(self, test_client):
        response = test_client.get("/tracks/9999")
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# Review CRUD
# ---------------------------------------------------------------------------

class TestReviewCRUD:
    """Tests for the full review lifecycle."""

    def test_create_review(self, test_client, auth_headers):
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "Test User",
                "rating": 4,
                "comment": "A beautiful and dreamy piece.",
            },
            headers=auth_headers,
        )
        assert response.status_code == 201
        data = response.json()
        assert data["rating"] == 4
        assert data["track_id"] == 1

    def test_create_review_invalid_track(self, test_client, auth_headers):
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 9999,
                "reviewer_name": "Nobody",
                "rating": 3,
                "comment": "This track does not exist.",
            },
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_create_review_invalid_rating(self, test_client, auth_headers):
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "Tester",
                "rating": 6,
                "comment": "Rating out of range.",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_list_reviews(self, test_client):
        response = test_client.get("/reviews")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_list_reviews_filter_by_track(self, test_client, auth_headers):
        test_client.post(
            "/reviews",
            json={
                "track_id": 2,
                "reviewer_name": "Filter Tester",
                "rating": 5,
                "comment": "Elegant and calm.",
            },
            headers=auth_headers,
        )
        response = test_client.get("/reviews?track_id=2")
        assert response.status_code == 200
        data = response.json()
        assert all(r["track_id"] == 2 for r in data)

    def test_list_reviews_filter_by_min_rating(self, test_client):
        response = test_client.get("/reviews?min_rating=4")
        assert response.status_code == 200
        data = response.json()
        assert all(r["rating"] >= 4 for r in data)

    def test_full_review_crud_flow(self, test_client, auth_headers):
        # Create
        create_resp = test_client.post(
            "/reviews",
            json={
                "track_id": 3,
                "reviewer_name": "CRUD Tester",
                "rating": 3,
                "comment": "Interesting rhythm.",
            },
            headers=auth_headers,
        )
        assert create_resp.status_code == 201
        review_id = create_resp.json()["id"]

        # Read
        get_resp = test_client.get(f"/reviews/{review_id}")
        assert get_resp.status_code == 200
        assert get_resp.json()["rating"] == 3

        # Update
        update_resp = test_client.put(
            f"/reviews/{review_id}",
            json={"rating": 5, "comment": "Actually, this is outstanding."},
            headers=auth_headers,
        )
        assert update_resp.status_code == 200
        assert update_resp.json()["rating"] == 5

        # Delete
        delete_resp = test_client.delete(f"/reviews/{review_id}", headers=auth_headers)
        assert delete_resp.status_code == 204

        # Verify deletion
        verify_resp = test_client.get(f"/reviews/{review_id}")
        assert verify_resp.status_code == 404

    def test_update_review_not_found(self, test_client, auth_headers):
        response = test_client.put(
            "/reviews/9999",
            json={"rating": 2},
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_delete_review_not_found(self, test_client, auth_headers):
        response = test_client.delete("/reviews/9999", headers=auth_headers)
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# Tag endpoints
# ---------------------------------------------------------------------------

class TestTagEndpoints:
    """Tests for user tag creation and listing."""

    def test_create_tag(self, test_client, auth_headers):
        response = test_client.post(
            "/tags",
            json={
                "track_id": 1,
                "tag_name": "peaceful",
                "created_by": "Tag Tester",
            },
            headers=auth_headers,
        )
        assert response.status_code == 201
        assert response.json()["tag_name"] == "peaceful"

    def test_create_duplicate_tag(self, test_client, auth_headers):
        test_client.post(
            "/tags",
            json={
                "track_id": 4,
                "tag_name": "unique-dup-test",
                "created_by": "Dup Tester",
            },
            headers=auth_headers,
        )
        response = test_client.post(
            "/tags",
            json={
                "track_id": 4,
                "tag_name": "unique-dup-test",
                "created_by": "Dup Tester",
            },
            headers=auth_headers,
        )
        assert response.status_code == 409

    def test_create_tag_invalid_track(self, test_client, auth_headers):
        response = test_client.post(
            "/tags",
            json={
                "track_id": 9999,
                "tag_name": "ghost",
                "created_by": "Nobody",
            },
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_list_tags(self, test_client):
        response = test_client.get("/tags")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_list_tags_by_track(self, test_client):
        response = test_client.get("/tags?track_id=1")
        assert response.status_code == 200
        data = response.json()
        assert all(t["track_id"] == 1 for t in data)

    def test_delete_tag(self, test_client, auth_headers):
        create_resp = test_client.post(
            "/tags",
            json={
                "track_id": 5,
                "tag_name": "to-delete",
                "created_by": "Deleter",
            },
            headers=auth_headers,
        )
        tag_id = create_resp.json()["id"]
        delete_resp = test_client.delete(f"/tags/{tag_id}", headers=auth_headers)
        assert delete_resp.status_code == 204

    def test_delete_tag_not_found(self, test_client, auth_headers):
        response = test_client.delete("/tags/9999", headers=auth_headers)
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# Collection endpoints
# ---------------------------------------------------------------------------

class TestCollectionEndpoints:
    """Tests for collection management."""

    def test_create_collection(self, test_client, auth_headers):
        response = test_client.post(
            "/collections",
            json={
                "name": "Test Collection Alpha",
                "description": "A test collection.",
                "created_by": "Collection Tester",
            },
            headers=auth_headers,
        )
        assert response.status_code == 201
        assert response.json()["name"] == "Test Collection Alpha"

    def test_create_duplicate_collection(self, test_client, auth_headers):
        test_client.post(
            "/collections",
            json={
                "name": "Duplicate Test Col",
                "created_by": "Tester",
            },
            headers=auth_headers,
        )
        response = test_client.post(
            "/collections",
            json={
                "name": "Duplicate Test Col",
                "created_by": "Tester",
            },
            headers=auth_headers,
        )
        assert response.status_code == 409

    def test_list_collections(self, test_client):
        response = test_client.get("/collections")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_collection_with_items(self, test_client, auth_headers):
        col_resp = test_client.post(
            "/collections",
            json={
                "name": "Items Test Collection",
                "description": "Testing item addition.",
                "created_by": "Item Tester",
            },
            headers=auth_headers,
        )
        col_id = col_resp.json()["id"]

        add_resp = test_client.post(
            f"/collections/{col_id}/items",
            json={"track_id": 1, "note": "Opening track."},
            headers=auth_headers,
        )
        assert add_resp.status_code == 201

        add_resp2 = test_client.post(
            f"/collections/{col_id}/items",
            json={"track_id": 2},
            headers=auth_headers,
        )
        assert add_resp2.status_code == 201

        detail = test_client.get(f"/collections/{col_id}").json()
        assert detail["item_count"] == 2
        assert len(detail["items"]) == 2

    def test_add_duplicate_track_to_collection(self, test_client, auth_headers):
        col_resp = test_client.post(
            "/collections",
            json={
                "name": "Dup Item Test",
                "created_by": "Tester",
            },
            headers=auth_headers,
        )
        col_id = col_resp.json()["id"]
        test_client.post(
            f"/collections/{col_id}/items",
            json={"track_id": 1},
            headers=auth_headers,
        )
        dup_resp = test_client.post(
            f"/collections/{col_id}/items",
            json={"track_id": 1},
            headers=auth_headers,
        )
        assert dup_resp.status_code == 409

    def test_add_track_to_nonexistent_collection(self, test_client, auth_headers):
        response = test_client.post(
            "/collections/9999/items",
            json={"track_id": 1},
            headers=auth_headers,
        )
        assert response.status_code == 404

    def test_delete_collection(self, test_client, auth_headers):
        col_resp = test_client.post(
            "/collections",
            json={
                "name": "To Delete Collection",
                "created_by": "Deleter",
            },
            headers=auth_headers,
        )
        col_id = col_resp.json()["id"]
        delete_resp = test_client.delete(f"/collections/{col_id}", headers=auth_headers)
        assert delete_resp.status_code == 204

    def test_delete_collection_not_found(self, test_client, auth_headers):
        response = test_client.delete("/collections/9999", headers=auth_headers)
        assert response.status_code == 404

    def test_get_collection_not_found(self, test_client):
        response = test_client.get("/collections/9999")
        assert response.status_code == 404


# ---------------------------------------------------------------------------
# Analytics endpoints
# ---------------------------------------------------------------------------

class TestAnalyticsEndpoints:
    """Tests for analytics and summary endpoints."""

    def test_top_rated_tracks(self, test_client, auth_headers):
        test_client.post(
            "/reviews",
            json={
                "track_id": 5,
                "reviewer_name": "Analytics User",
                "rating": 5,
                "comment": "Spacious and beautiful ambient track.",
            },
            headers=auth_headers,
        )
        response = test_client.get("/analytics/top-rated-tracks")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if len(data) > 0:
            assert "title" in data[0]
            assert "average_rating" in data[0]
            assert "review_count" in data[0]

    def test_genre_summary(self, test_client):
        response = test_client.get("/analytics/genre-summary")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 5
        assert "genre_name" in data[0]
        assert "track_count" in data[0]

    def test_top_tags(self, test_client):
        response = test_client.get("/analytics/top-tags")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_mood_distribution(self, test_client):
        response = test_client.get("/analytics/mood-distribution")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        if len(data) > 0:
            assert "mood" in data[0]
            assert "track_count" in data[0]

    def test_review_activity(self, test_client):
        response = test_client.get("/analytics/review-activity")
        assert response.status_code == 200
        data = response.json()
        assert "total_reviews" in data
        assert "average_rating" in data
        assert "reviewers" in data


# ---------------------------------------------------------------------------
# Authentication tests
# ---------------------------------------------------------------------------

class TestAuthentication:
    """Tests for API key authentication on write operations."""

    def test_create_review_without_api_key(self, test_client):
        """Write operations should return 401 without an API key."""
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "No Auth",
                "rating": 3,
                "comment": "Should be rejected.",
            },
        )
        assert response.status_code == 401
        body = response.json()
        assert body["error"] == "authentication_required"

    def test_create_review_with_invalid_api_key(self, test_client):
        """Write operations should return 403 with an invalid API key."""
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "Bad Key",
                "rating": 3,
                "comment": "Should be rejected.",
            },
            headers={"X-API-Key": "invalid-key-12345"},
        )
        assert response.status_code == 403
        body = response.json()
        assert body["error"] == "invalid_api_key"

    def test_create_tag_without_api_key(self, test_client):
        """Tag creation should require authentication."""
        response = test_client.post(
            "/tags",
            json={
                "track_id": 1,
                "tag_name": "no-auth-tag",
                "created_by": "Nobody",
            },
        )
        assert response.status_code == 401

    def test_delete_review_without_api_key(self, test_client):
        """Delete operations should require authentication."""
        response = test_client.delete("/reviews/1")
        assert response.status_code == 401

    def test_create_collection_without_api_key(self, test_client):
        """Collection creation should require authentication."""
        response = test_client.post(
            "/collections",
            json={
                "name": "Unauth Collection",
                "created_by": "Nobody",
            },
        )
        assert response.status_code == 401

    def test_read_endpoints_remain_public(self, test_client):
        """GET endpoints should NOT require authentication."""
        public_endpoints = [
            "/",
            "/health",
            "/genres",
            "/tracks",
            "/reviews",
            "/tags",
            "/collections",
            "/analytics/genre-summary",
            "/analytics/top-tags",
            "/analytics/mood-distribution",
            "/analytics/review-activity",
        ]
        for endpoint in public_endpoints:
            response = test_client.get(endpoint)
            assert response.status_code == 200, f"GET {endpoint} should be public but returned {response.status_code}"


# ---------------------------------------------------------------------------
# Validation edge cases
# ---------------------------------------------------------------------------

class TestValidation:
    """Tests for input validation and error handling."""

    def test_review_comment_too_short(self, test_client, auth_headers):
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "Validator",
                "rating": 3,
                "comment": "ab",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_review_rating_too_low(self, test_client, auth_headers):
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "Validator",
                "rating": 0,
                "comment": "Rating zero is invalid.",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_tag_name_too_long(self, test_client, auth_headers):
        response = test_client.post(
            "/tags",
            json={
                "track_id": 1,
                "tag_name": "x" * 51,
                "created_by": "Validator",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_collection_name_empty(self, test_client, auth_headers):
        response = test_client.post(
            "/collections",
            json={
                "name": "",
                "created_by": "Validator",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422

    def test_tracks_limit_exceeds_max(self, test_client):
        response = test_client.get("/tracks?limit=200")
        assert response.status_code == 422

    def test_structured_error_response_format(self, test_client, auth_headers):
        """Verify that validation errors return structured JSON with details."""
        response = test_client.post(
            "/reviews",
            json={
                "track_id": 1,
                "reviewer_name": "Validator",
                "rating": 0,
                "comment": "ab",
            },
            headers=auth_headers,
        )
        assert response.status_code == 422
        body = response.json()
        assert "error" in body
        assert body["error"] == "validation_error"
        assert "details" in body
        assert isinstance(body["details"], list)
        assert len(body["details"]) >= 1
