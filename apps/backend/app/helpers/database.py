from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.helpers.settings import settings

__engine = create_engine(settings.DATABASE_URL)
'''データベースのエンジン'''
session_local = sessionmaker(autocommit=False, autoflush=False, bind=__engine)
'''データベースのセッション'''

def get_database() -> Session: # type: ignore
    '''
    データベースのセッションを取得
    :return: Session: データベースのセッション
    '''
    database = session_local()
    try:
        yield database
    finally:
        database.close()