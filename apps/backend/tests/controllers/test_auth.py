import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.main import app
from app.models.user import User as UserModel
from app.config.hash import Hash
from app.config.database import get_db

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def mock_db():
    with patch("app.config.database.SessionLocal") as mock_session:
        mock_db = MagicMock()
        mock_session.return_value = mock_db
        yield mock_db

@pytest.fixture
def setup_mock_db(mock_db):
    # モックデータベースのセットアップ
    user = UserModel(username="testuser", password=Hash().get_password_hash("testpassword"))
    mock_db.query.return_value.filter.return_value.first.return_value = user
    yield

def test_login(client, setup_mock_db):
    response = client.post("/auth/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_read_users_me(client, setup_mock_db):
    login_response = client.post("/auth/token", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/auth/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"username": "testuser"}

def test_logout(client, setup_mock_db):
    login_response = client.post("/auth/token", data={"username": "testuser", "password": "testpassword"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/auth/logout", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"msg": "Successfully logged out"}