from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from app.models.base_model import BaseModel
from app.utils.datetime import DateTimeUtil
# from app.utils.hash import verify_password

class User(BaseModel):
    '''
    ユーザー情報
    '''
    __tablename__ = "users"
    uuid: Mapped[str] = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    username: Mapped[str] = Column(String(60), nullable=False)
    email: Mapped[str] = Column(String(256), nullable=False)
    password: Mapped[str] = Column(String(256), nullable=False)
    role_cls: Mapped[str] = Column(String(2), nullable=False)
    from_date: Mapped[datetime] = Column(DateTime, nullable=False)
    to_date: Mapped[datetime] = Column(DateTime, nullable=True, default=None)
    created_at: Mapped[datetime] = Column(DateTime, default=lambda: DateTimeUtil.now())
    updated_at: Mapped[datetime] = Column(DateTime, default=lambda: DateTimeUtil.now(), onupdate=lambda: DateTimeUtil.now())

    # def verify_password(self, plain_password: str) -> bool:
    #     '''
    #     パスワードを検証します
    #     :param plain_password: str: 検証するパスワード
    #     :return: bool: パスワードが一致する場合はTrue
    #     '''
    #     return verify_password(plain_password, self.password)
