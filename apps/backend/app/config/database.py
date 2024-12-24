#
# データベース接続
#
# from fastapi import FastAPI
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session

# # グローバルスコープでSessionLocalを定義
# SessionLocal = None

# def connect_db(app: FastAPI):
#     global SessionLocal
#     engine = create_engine(app.state.settings.database_url)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     app.state.db = SessionLocal()

# def close_db(app: FastAPI):
#     app.state.db.close()
#     app.state.db = None

# def get_db() -> Session:
#     global SessionLocal
#     if SessionLocal is None:
#         raise ValueError("SessionLocal is not initialized. Call connect_db first.")
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"database_url: {settings.database_url}")  # ログ出力
# DATABASE_URL = "sqlite:///./test.db"  # 必要に応じてデータベースURLを設定

# エンジンとセッションの設定
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()