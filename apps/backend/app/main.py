# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"message": "Hell, FastAPI!"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!!"}

@app.get("/api/data")
async def get_data():
    return {"data": "This is some data from FastAPI!!"}
