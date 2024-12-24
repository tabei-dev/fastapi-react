# import os
import redis
import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta
from dotenv import load_dotenv
from app.config.settings import settings

# load_dotenv()  # .envファイルから環境変数を読み込む

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Redisに接続
r = redis.Redis(host='redis', port=6379, db=0)

# SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    password: str

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "password": "secret"
    }
}

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # トークンがブラックリストにあるか確認
    if r.get(token):
        raise HTTPException(status_code=401, detail="Token has been revoked")
    
    return token_data

@app.post("/token", response_model=Token)
async def login(user: User):
    user_dict = fake_users_db.get(user.username)
    if not user_dict or user_dict["password"] != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    token_data = verify_token(token)
    return {"username": token_data.username}

@app.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    # トークンをブラックリストに追加
    r.set(token, "revoked", ex=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    return {"msg": "Successfully logged out"}