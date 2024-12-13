from datetime import datetime, timezone
# from pydantic import BaseModel
from .model_base import ModelBase
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_utils import UUIDType
from uuid import uuid4

#
# Userモデルクラス
#
class User(ModelBase):
    __tablename__ = "users"
    # id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    username = Column(String(60), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(60), nullable=False)
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=True, default=None)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

# class User(BaseModel):
#     id: int
#     username: str
#     email: str
#     password: str
#     from_date: datetime
#     to_date: datetime
#     created_at: datetime
#     updated_at: datetime