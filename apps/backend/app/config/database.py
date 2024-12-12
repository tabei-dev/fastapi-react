#
# データベース接続
#
from fastapi import FastAPI
import psycopg2
from app.config.settings import settings

def connect_db(app: FastAPI):
    if app.state.settings.database_url:
        app.state.db = psycopg2.connect(app.state.settings.database_url)
    else:
        raise ValueError("DATABASE_URL is not set")

def close_db(app: FastAPI):
    app.state.db.close()