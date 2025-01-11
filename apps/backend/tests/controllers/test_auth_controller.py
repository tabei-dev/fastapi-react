import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app
from app.controllers.auth_controller import router as auth_router
from app.services.auth_service import auth_service
from app.utils.hash import HashUtil

client = TestClient(app)

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def mock_db():
    with patch("app.config.database.SessionLocal") as mock_session:
        mock_db = MagicMock()
        mock_user = MagicMock()
        mock_user.username = "testuser"
        mock_user.password = HashUtil().get_hashed_password("testpassword")
        mock_session.return_value.query().filter().first.return_value = mock_user
        yield mock_db

def test_login_success(client, mock_db):
    response = client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_read_users_me(client, mock_db):
    login_response = client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/auth/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"username": "testuser"}

def test_logout(client, mock_db):
    login_response = client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/auth/logout", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"msg": "Successfully logged out"}