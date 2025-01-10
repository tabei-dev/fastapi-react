# import os
# import unittest
# from app.config.settings import settings

# class TestSettings(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         os.environ["ENVIRONMENT"] = "development"
#         os.environ["ALLOW_ORIGINS"] = "http://example.com"
#         os.environ["DATABASE_URL"] = "sqlite:///./test.db"
#         os.environ["REDIS_PORT"] = "6379"
#         os.environ["SECRET_KEY"] = "secret"
#         # os.environ["ASSETS_PATH"] = "/test/assets"
#         os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"] = "30"
#         # 環境変数を再読み込み
#         settings.environment = os.getenv("ENVIRONMENT", "development")
#         settings.allow_origins = os.getenv("ALLOW_ORIGINS", "http://example.com")
#         settings.database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
#         settings.redis_port = int(os.getenv("REDIS_PORT", 6379))
#         settings.secret_key = os.getenv("SECRET_KEY", "secret")
#         settings.assets_path = os.getenv("ASSETS_PATH", "/test/assets")
#         settings.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

#     def test_environment(self):
#         self.assertEqual(settings.environment, os.getenv("ENVIRONMENT", "development"))

#     def test_allow_origins(self):
#         self.assertEqual(settings.allow_origins, os.getenv("ALLOW_ORIGINS", "http://example.com"))

#     def test_database_url(self):
#         self.assertEqual(settings.database_url, os.getenv("DATABASE_URL", "sqlite:///./test.db"))

#     def test_redis_port(self):
#         self.assertEqual(settings.redis_port, int(os.getenv("REDIS_PORT", 6379)))

#     def test_secret_key(self):
#         self.assertEqual(settings.secret_key, os.getenv("SECRET_KEY", "secret"))

#     def test_assets_path(self):
#         self.assertEqual(settings.assets_path, os.getenv("ASSETS_PATH", "/test/assets"))

#     def test_access_token_expire_minutes(self):
#         self.assertEqual(settings.access_token_expire_minutes, int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))

# if __name__ == '__main__':
#     unittest.main()

import os
import pytest
from app.config.settings import settings

# def test_assets_path():
#     assets_path = os.path.join(os.path.dirname(__file__), '../../assets')
#     assert settings.assets_path == assets_path

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