#
# .envより環境変数を取得
#
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

#
# 環境変数取得クラス
#
class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "development")
    allow_origins: str = os.getenv("ALLOW_ORIGINS", "http://example.com")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '../..', '.env'))

settings = Settings()