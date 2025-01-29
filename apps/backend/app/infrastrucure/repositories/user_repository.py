from sqlalchemy.orm import Session
from app.infrastrucure.dtos.user_dto import UserDTO

def fetch_user(db: Session, username: str) -> UserDTO:
    user_dto = db.query(UserDTO).filter(UserDTO.username == username).first()
    if user_dto:
        return user_dto
    else:
        raise Exception(f'ユーザー {username} に該当する UserDTO が見つかりませんでした')