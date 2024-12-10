import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    allow_origins: str = "http://example.com"  # デフォルト値

    model_config = ConfigDict(env_file=os.path.join(os.path.dirname(__file__), '../..', '.env'))

settings = Settings()