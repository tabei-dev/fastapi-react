import sys
import os

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from fastapi import FastAPI
# from app.config.settings import settings
from app.config.database import connect_db, close_db
from app.config.hash import Hash
from app.models.user import User

class Settings:
    database_url = "postgresql://sa:sa0000@db:5432/fastapi_db"

def seed():
    app = FastAPI()
    app.state.settings = Settings()
    connect_db(app)

    hash = Hash()

    app.state.db.add_all([
        User(
            username="testuser1",
            email="testuser1@examples.com",
            password=hash.get_password_hash("password1"),
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
        User(
            username="testuser2",
            email="testuser2@examples.com",
            password=hash.get_password_hash("password2"),
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
    ])

    app.state.db.commit()

    close_db(app)

if __name__ == "__main__":
    seed()