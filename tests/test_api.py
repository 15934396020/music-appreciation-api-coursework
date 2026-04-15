from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_tracks_endpoint_returns_seeded_data():
    response = client.get("/tracks?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "title" in data[0]
    assert "genre" in data[0]


def test_review_crud_flow():
    create_response = client.post(
        "/reviews",
        json={
            "track_id": 2,
            "reviewer_name": "Test Reviewer",
            "rating": 4,
            "comment": "Elegant and calm.",
        },
    )
    assert create_response.status_code == 201
    review = create_response.json()
    review_id = review["id"]

    get_response = client.get(f"/reviews/{review_id}")
    assert get_response.status_code == 200
    assert get_response.json()["rating"] == 4

    update_response = client.put(
        f"/reviews/{review_id}",
        json={"rating": 5, "comment": "Elegant, calm, and memorable."},
    )
    assert update_response.status_code == 200
    assert update_response.json()["rating"] == 5

    delete_response = client.delete(f"/reviews/{review_id}")
    assert delete_response.status_code == 204


def test_tag_and_collection_endpoints():
    tag_response = client.post(
        "/tags",
        json={
            "track_id": 1,
            "tag_name": "impressionistic",
            "created_by": "Tag Tester",
        },
    )
    assert tag_response.status_code == 201

    list_tag_response = client.get("/tags?track_id=1")
    assert list_tag_response.status_code == 200
    assert any(tag["tag_name"] == "impressionistic" for tag in list_tag_response.json())

    collection_response = client.post(
        "/collections",
        json={
            "name": "Late Night Listening",
            "description": "Calm and reflective tracks for evening study.",
            "created_by": "Collection Tester",
        },
    )
    assert collection_response.status_code == 201
    collection_id = collection_response.json()["id"]

    add_item_response = client.post(
        f"/collections/{collection_id}/items",
        json={"track_id": 1, "note": "Strong opening mood."},
    )
    assert add_item_response.status_code == 201

    detail_response = client.get(f"/collections/{collection_id}")
    assert detail_response.status_code == 200
    assert detail_response.json()["item_count"] == 1


def test_analytics_endpoint():
    client.post(
        "/reviews",
        json={
            "track_id": 3,
            "reviewer_name": "Analytics User",
            "rating": 5,
            "comment": "Rhythmically distinctive and highly enjoyable.",
        },
    )
    response = client.get("/analytics/top-rated-tracks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
