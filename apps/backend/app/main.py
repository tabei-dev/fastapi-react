import psycopg2
# from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from pydantic import ValidationError
# from app.config.database import connect_db, close_db
from app.helpers.logging import logger
from app.helpers.settings import settings
from app.routers.auth_router import router as auth_router
from app.errors.validation_error import ValidationError
# from app.services.classification_service import classification_service
# from app.services.message_service import message_service

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # logger.info('アプリケーション開始...')
#     # classification_service
#     # initialize_messages()
#     # yield
#     pass

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

logger.debug(f"ログ:ALLOW_ORIGINS: {settings.ALLOW_ORIGINS}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOW_ORIGINS],
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

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    logger.debug(f"到達:ValidationError: {exc.message}")
    return JSONResponse(
        status_code=422,
        content={"message": exc.message}
    )
