from app.core.security import get_password_hash
from app.models.user import User
from app.core.config import settings
from jose import jwt


def test_register_and_login(client):
    response = client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={"email": "user@example.com", "password": "Pass1234", "full_name": "User"},
    )
    assert response.status_code == 200

    response = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": "user@example.com", "password": "Pass1234"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_refresh_token(client):
    client.post(
        f"{settings.API_V1_STR}/auth/register",
        json={"email": "refresh@example.com", "password": "Pass1234", "full_name": "User"},
    )
    login = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": "refresh@example.com", "password": "Pass1234"},
    )
    refresh_token = login.json()["refresh_token"]
    response = client.post(f"{settings.API_V1_STR}/auth/refresh", params={"token": refresh_token})
    assert response.status_code == 200


def test_invalid_login(client):
    response = client.post(
        f"{settings.API_V1_STR}/auth/login",
        data={"username": "nope@example.com", "password": "bad"},
    )
    assert response.status_code == 401
