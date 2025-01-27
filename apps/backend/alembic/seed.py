import sys
import os

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from app.helpers.database import session_local
from app.helpers.hash import to_hashed_password
from app.infrastrucure.dtos.user_dto import UserDTO

def seed():
    database = session_local()

    database.add_all([
        UserDTO(
            username="admin",
            email="admin@examples.com",
            hashed_password=to_hashed_password("admin0000"),
            role_cls="00",
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
        UserDTO(
            username="Kyoko Otonashi",
            email="ikkoku00@examples.com",
            hashed_password=to_hashed_password("kyoko0000"),
            role_cls="00",
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
        UserDTO(
            username="Yusaku Godai",
            email="ikkoku05@examples.com",
            hashed_password=to_hashed_password("yusaku0000"),
            role_cls="01",
            from_date=datetime(2024, 12, 13),
            to_date=None,
        ),
    ])

    database.commit()
    database.close()

if __name__ == "__main__":
    seed()