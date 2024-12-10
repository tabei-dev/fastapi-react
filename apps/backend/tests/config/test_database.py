import pytest
from fastapi import FastAPI
from app.config.settings import Settings
from app.config.database import connect_db, close_db

class MockSettings:
    database_url = settings.database_url

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