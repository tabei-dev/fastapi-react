from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from app.helpers.datetime import get_now
from app.infrastrucure.dtos.base_model import BaseModel

class UserDTO(BaseModel):
    __tablename__ = "users"
    uuid: Mapped[str] = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    username: Mapped[str] = Column(String(60), nullable=False)
    email: Mapped[str] = Column(String(256), nullable=False)
    hashed_password: Mapped[str] = Column(String(256), nullable=False)
    role_cls: Mapped[str] = Column(String(2), nullable=False)
    from_date: Mapped[datetime] = Column(DateTime, nullable=False)
    to_date: Mapped[datetime] = Column(DateTime, nullable=True, default=None)
    created_at: Mapped[datetime] = Column(DateTime, default=lambda: get_now())
    updated_at: Mapped[datetime] = Column(DateTime, default=lambda: get_now(), onupdate=lambda: get_now())
