import os
import pytest
from app.helpers.settings import settings

def test_environment_variable(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.setenv("ALLOW_ORIGINS", "http://example.org")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    monkeypatch.setenv("REDIS_PORT", "6380")
    monkeypatch.setenv("SECRET_KEY", "newsecret")
    monkeypatch.setenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")

    settings.ENVIRONMENT = os.getenv("ENVIRONMENT")
    settings.ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS")
    settings.DATABASE_URL = os.getenv("DATABASE_URL")
    settings.REDIS_PORT = int(os.getenv("REDIS_PORT"))
    settings.SECRET_KEY = os.getenv("SECRET_KEY")
    settings.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    assert settings.ENVIRONMENT == "production"
    assert settings.ALLOW_ORIGINS == "http://example.org"
    assert settings.DATABASE_URL == "postgresql://user:password@localhost/dbname"
    assert settings.REDIS_PORT == 6380
    assert settings.SECRET_KEY == "newsecret"
    assert settings.ACCESS_TOKEN_EXPIRE_MINUTES == 60