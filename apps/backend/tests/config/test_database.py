import pytest
from fastapi import FastAPI
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.sql import text
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
    assert app.state.db is not None
    close_db(app)
    # with pytest.raises(InvalidRequestError):
    #     app.state.db.execute(text("SELECT 1"))
    assert app.state.db is None