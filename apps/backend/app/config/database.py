import psycopg2
from app.config.settings import settings

def connect_db(app):
    app.state.db = psycopg2.connect(settings.database_url)

def close_db(app):
    app.state.db.close()