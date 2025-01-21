import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app
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
        mock_user.email = "testuser@example.com"
        mock_user.role_cls = "user"
        mock_session.return_value.query().filter().first.return_value = mock_user
        yield mock_db

def test_login_is_successful(client, mock_db):
    response = client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200

def test_login_is_unsuccessful(client, mock_db):
    response = client.post("/auth/login", data={"username": "invalid_user", "password": "invalid_password"})
    assert response.status_code == 422

def test_logout_is_successful(client, mock_db):
    login_response = client.post("/auth/login", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/auth/logout", headers=headers)
    assert response.status_code == 200

def test_logout_is_unsuccessful(client, mock_db):
    response = client.post("/auth/logout")
    assert response.status_code == 401
