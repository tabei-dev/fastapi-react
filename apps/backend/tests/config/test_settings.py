import os
from app.config.settings import Settings
# from pydantic import BaseSettings

def test_settings_env_allow_origins(monkeypatch):
    monkeypatch.setenv("ALLOW_ORIGINS", "http://localhost:3000")
    settings = Settings()
    assert settings.allow_origins == "http://localhost:3000"

def test_settings_env_database_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://sa:sa0000@localhost:5432/fastapi_db")
    settings = Settings()
    assert settings.database_url == "postgresql://sa:sa0000@localhost:5432/fastapi_db"