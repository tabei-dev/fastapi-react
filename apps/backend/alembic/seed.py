import sys
import os

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from app.config.database import SessionLocal
from app.models.user import User
from app.utils.hash import get_hashed_password

def seed():
    db = SessionLocal()

    db.add_all([
        User(
            username="admin",
            email="admin@examples.com",
            password=get_hashed_password("admin0000"),
            role_cls="00",
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
        User(
            username="Kyoko Otonashi",
            email="ikkoku00@examples.com",
            password=get_hashed_password("kyoko0000"),
            role_cls="00",
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
        User(
            username="Yusaku Godai",
            email="ikkoku05@examples.com",
            password=get_hashed_password("yusaku0000"),
            role_cls="01",
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
    ])

    db.commit()
    db.close()

if __name__ == "__main__":
    seed()