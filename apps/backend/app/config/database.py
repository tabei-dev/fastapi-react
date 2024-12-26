from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config.settings import settings

engine = create_engine(settings.database_url)
'''
データベースのエンジン
'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
'''
データベースのセッション
'''

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