from app.core.config import settings


def test_ai_generate(client):
    payload = {
        "project_name": "Demo",
        "description": "Un site demo",
        "primary_resource": "projets",
    }
    response = client.post(f"{settings.API_V1_STR}/ai/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["project_slug"] == "demo"
    assert data["files"]
