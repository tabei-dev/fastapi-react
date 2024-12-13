from datetime import datetime, timezone
from .model_base import ModelBase
from sqlalchemy import Column, String, DateTime
from sqlalchemy_utils import UUIDType
from uuid import uuid4
from typing import Optional
from sqlalchemy.orm import Mapped

class User(ModelBase):
    __tablename__ = "users"
    uuid: Mapped[str] = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    username: Mapped[str] = Column(String(60), nullable=False)
    email: Mapped[str] = Column(String(256), nullable=False)
    password: Mapped[str] = Column(String(60), nullable=False)
    from_date: Mapped[datetime] = Column(DateTime, nullable=False)
    to_date: Mapped[Optional[datetime]] = Column(DateTime, nullable=True, default=None)
    created_at: Mapped[datetime] = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))