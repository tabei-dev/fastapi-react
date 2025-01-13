import os
import pytest
from app.config.settings import settings

def test_environment_variable(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.setenv("ALLOW_ORIGINS", "http://example.org")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    monkeypatch.setenv("REDIS_PORT", "6380")
    monkeypatch.setenv("SECRET_KEY", "newsecret")
    monkeypatch.setenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")

    settings.environment = os.getenv("ENVIRONMENT")
    settings.allow_origins = os.getenv("ALLOW_ORIGINS")
    settings.database_url = os.getenv("DATABASE_URL")
    settings.redis_port = int(os.getenv("REDIS_PORT"))
    settings.secret_key = os.getenv("SECRET_KEY")
    settings.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    assert settings.environment == "production"
    assert settings.allow_origins == "http://example.org"
    assert settings.database_url == "postgresql://user:password@localhost/dbname"
    assert settings.redis_port == 6380
    assert settings.secret_key == "newsecret"
    assert settings.access_token_expire_minutes == 60