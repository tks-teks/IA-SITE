from app.core.config import settings
from app.models.user import User
from app.core.security import get_password_hash
from tests.conftest import TestingSessionLocal


def admin_headers(client):
    db = TestingSessionLocal()
    try:
        admin = User(email="admin@example.com", hashed_password=get_password_hash("Admin1234"), role="admin")
        db.add(admin)
        db.commit()
    finally:
        db.close()

    login = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": "admin@example.com", "password": "Admin1234"},
    )
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_admin_stats_requires_admin(client):
    response = client.get(f"{settings.API_V1_STR}/admin/stats")
    assert response.status_code in (401, 403)


def test_admin_stats(client):
    headers = admin_headers(client)
    response = client.get(f"{settings.API_V1_STR}/admin/stats", headers=headers)
    assert response.status_code == 200
    assert "users" in response.json()
