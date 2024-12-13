from fastapi import FastAPI
from app.config.settings import settings
from app.config.database import connect_db, close_db
from app.database.models.user import User

class Settings:
    database_url = settings.database_url

def seed():
    app = FastAPI()
    app.state.settings = Settings()
    connect_db(app)

    user = User()

    app.state.db.commit

    close_db(app)

if __name__ == "__main__":
    seed()