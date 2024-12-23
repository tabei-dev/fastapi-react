#
# データベース接続
#
from fastapi import FastAPI
# import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_db(app: FastAPI):
    # if app.state.settings.database_url:
    #     app.state.db = psycopg2.connect(app.state.settings.database_url)
    # else:
    #     raise ValueError("DATABASE_URL is not set")
    engine = create_engine(app.state.settings.database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    app.state.db = SessionLocal()

def close_db(app: FastAPI):
    app.state.db.close()
    app.state.db = None