import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)

    print("GET API test passed")


def test_create_post():
    payload = {
        "title": "Automation Testing",
        "body": "Learning Python API automation",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=15
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    print("POST API test passed")


def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Automation Test",
        "body": "API testing with Python",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload,
        timeout=15
    )

    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]

    print("PUT API test passed")


def test_delete_post():
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    print("DELETE API test passed")


def test_post_not_found():
    response = requests.get(
        f"{BASE_URL}/posts/999999",
        timeout=15
    )

    assert response.status_code == 404

    print("Negative API test passed")
