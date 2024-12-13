import sys
import os

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from fastapi import FastAPI
# from app.config.settings import settings
from app.config.database import connect_db, close_db
from app.database.models.user import User

class Settings:
    database_url = "postgresql://sa:sa0000@db:5432/fastapi_db"

def seed():
    app = FastAPI()
    app.state.settings = Settings()
    connect_db(app)

    user = User(
        username="tabei",
        email="tabei.dev@gmail.com",
        password="5155",
        from_date=datetime(2024, 12, 13),
        to_date=None,
    )

    app.state.db.add(user)

    app.state.db.commit()

    close_db(app)

if __name__ == "__main__":
    seed()