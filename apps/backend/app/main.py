import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.config.database import connect_db, close_db
from app.config.settings import settings
from app.routes.auth_router import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.allow_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup_event():
#     connect_db(app)

# @app.on_event("shutdown")
# async def shutdown_event():
#     close_db(app)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!!"}

@app.get("/api/data")
async def get_data():
    return {"data": "This is some data from FastAPI!!!"}

# app.mount("/auth", auth_app)
app.include_router(auth_router, prefix="/auth")