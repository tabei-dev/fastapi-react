# from typing import Any
# from sqlalchemy.ext.declarative import declared_attr
# from sqlalchemy.orm import as_declarative
from sqlalchemy.ext.declarative import declarative_base

# @as_declarative()
# class ModelBase:
#     id: Any
#     __name__: str

#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower

ModelBase = declarative_base()