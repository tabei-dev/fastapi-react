#
# .envより環境変数を取得
#
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    allow_origins: str = os.getenv("ALLOW_ORIGINS", "http://example.com")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '../..', '.env')

settings = Settings()