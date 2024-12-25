import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from app.config.settings import settings
from app.config.database import get_db

class MockSettings:
    database_url = "postgresql://sa:sa0000@db:5432/fastapi_db"

@pytest.fixture(scope="module")
def engine():
    return create_engine(MockSettings.database_url)

@pytest.fixture(scope="module")
def SessionLocal(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db(SessionLocal):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_get_db(db):
    assert db is not None
    result = db.execute(text("SELECT 1"))
    assert result.scalar() == 1