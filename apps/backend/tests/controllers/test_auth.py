import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.controllers.auth import create_access_token, verify_token, fake_users_db
from app.config.hash import Hash

client = TestClient(app)

# テスト用のユーザーを追加
fake_users_db["johndoe"] = {
    "username": "johndoe",
    "password": Hash().get_password_hash("secret")
}

def test_create_access_token():
    data = {"sub": "johndoe"}
    token = create_access_token(data)
    assert token is not None

def test_verify_token():
    data = {"sub": "johndoe"}
    token = create_access_token(data)
    token_data = verify_token(token)
    assert token_data.username == "johndoe"

def test_login_success():
    response = client.post("/auth/token", json={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_failure():
    response = client.post("/auth/token", json={"username": "johndoe", "password": "wrongpassword"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect username or password"}

def test_logout():
    data = {"sub": "johndoe"}
    token = create_access_token(data)
    response = client.post("/auth/logout", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Successfully logged out"}