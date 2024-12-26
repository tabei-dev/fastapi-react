import sys
import os

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from app.config.database import SessionLocal
from app.models.user import User
from app.utils.hash import Hash

def seed():
    db = SessionLocal()

    hash = Hash()

    db.add_all([
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

    db.commit()
    db.close()

if __name__ == "__main__":
    seed()