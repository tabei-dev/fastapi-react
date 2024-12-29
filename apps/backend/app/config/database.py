from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.config.settings import settings

engine = create_engine(settings.database_url)
'''
データベースのエンジン
'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# '''
# データベースのセッション
# '''
# Base = declarative_base()

# async def init_db() -> None:
#     '''
#     データベースの初期化
#     '''
#     # from app.models.user import Base
#     # Base.metadata.create_all(bind=engine)
#     print("データベースを初期化します")
#     async with engine.begin() as conn:
#         # 既存のテーブルを削除
#         await conn.run_sync(Base.metadata.drop_all)
#         # テーブルを作成
#         await conn.run_sync(Base.metadata.create_all)

def get_db() -> Session: # type: ignore
    '''
    データベースのセッションを取得
    :return: Session: データベースのセッション
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()