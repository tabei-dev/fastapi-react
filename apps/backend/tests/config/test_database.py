import pytest
from fastapi import FastAPI
from app.config.database import connect_db, close_db

class MockSettings:
    database_url = "postgresql://sa:sa0000@db:5432/fastapi_db"

@pytest.fixture
def app():
    app = FastAPI()
    app.state.settings = MockSettings()
    return app

def test_connect_db(app):
    connect_db(app)
    assert app.state.db is not None
    app.state.db.close()

def test_close_db(app):
    connect_db(app)
    close_db(app)
    assert app.state.db.closed