import os
from app.config.settings import Settings
# from pydantic import BaseSettings

def test_settings_env_var(monkeypatch):
    # 環境変数が設定されている場合の値をテスト
    monkeypatch.setenv("ALLOW_ORIGINS", "http://localhost:3000")
    settings = Settings()
    assert settings.allow_origins == "http://localhost:3000"

# def test_settings_default(monkeypatch):
#     # 環境変数が設定されていない場合のデフォルト値をテスト
#     settings = Settings()
#     assert settings.allow_origins == "http://example.com"
