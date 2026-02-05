from app.core.config import settings


def auth_header(client, email="project@example.com"):
    client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={"email": email, "password": "Pass1234", "full_name": "User"},
    )
    login = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": email, "password": "Pass1234"},
    )
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_project_crud(client):
    headers = auth_header(client)
    create = client.post(
        f"{settings.API_V1_STR}/projects/",
        json={"name": "Alpha", "description": "Test"},
        headers=headers,
    )
    assert create.status_code == 200
    project_id = create.json()["id"]

    list_response = client.get(f"{settings.API_V1_STR}/projects/", headers=headers)
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    update = client.put(
        f"{settings.API_V1_STR}/projects/{project_id}",
        json={"status": "published"},
        headers=headers,
    )
    assert update.status_code == 200

    delete = client.delete(f"{settings.API_V1_STR}/projects/{project_id}", headers=headers)
    assert delete.status_code == 200


def test_project_search(client):
    headers = auth_header(client, email="search@example.com")
    client.post(
        f"{settings.API_V1_STR}/projects/",
        json={"name": "Beta", "description": "Searchable"},
        headers=headers,
    )
    response = client.get(f"{settings.API_V1_STR}/projects/?query=Beta", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
