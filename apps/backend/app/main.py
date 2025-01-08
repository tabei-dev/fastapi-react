import psycopg2
# from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from pydantic import ValidationError
# from app.config.database import connect_db, close_db
from app.config.settings import settings
from app.controllers.auth_controller import router as auth_router
# from app.services.classification_service import classification_service
# from app.services.message_service import message_service
import logging

logger = logging.getLogger(__name__)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # logger.info('アプリケーション開始...')
#     # classification_service
#     # initialize_messages()
#     # yield
#     pass

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.allow_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!!"}

@app.get("/api/data")
async def get_data():
    return {"data": "This is some data from FastAPI!!!"}

# app.mount("/auth", auth_app)
app.include_router(auth_router, prefix="/auth")

@app.exception_handler(HTTPException)
async def validation_exception_handler(exc: HTTPException):
    logger.error(f"到達:HTTPException: {exc.detail}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.model}
    )
