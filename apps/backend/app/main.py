import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.auth import app as auth_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.allow_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     app.state.db = psycopg2.connect(settings.database_url)

# @app.on_event("shutdown")
# async def shutdown():
#     app.state.db.close()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!!"}

@app.get("/api/data")
async def get_data():
    return {"data": "This is some data from FastAPI!!!"}

app.mount("/auth", auth_app)