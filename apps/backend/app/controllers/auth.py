# import logging
import redis as Redis
import jwt
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.config.database import get_db
from app.config.hash import Hash
from app.config.settings import settings
from app.models.user import User as UserModel

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

app = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Redisに接続
redis = Redis.Redis(host='redis', port=6379, db=0)

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    '''
    トークンのレスポンスモデル
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    '''
    access_token: str
    token_type: str

class TokenData(BaseModel):
    '''
    トークンのペイロード
    :param username: str | None: ユーザー名
    '''
    username: str | None = None

class User(BaseModel):
    '''
    ユーザーのモデル
    :param username: str: ユーザー名
    :param password: str: パスワード
    '''
    username: str
    password: str

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    '''
    トークンを生成する
    :param data: dict: ペイロード
    :param expires_delta: timedelta | None: 有効期限
    :return: str: トークン
    '''
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # トークンがブラックリストにあるか確認
    if redis.get(token):
        raise HTTPException(status_code=401, detail="Token has been revoked")

    return token_data

@app.post("/token", response_model=Token)
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Token:
    '''
    ログイン
    :param response: Response: レスポンス
    :param form_data: OAuth2PasswordRequestForm: フォームデータ
    :param db: Session: DBセッション
    :return: Token: トークン
    '''
    # logger.info(f"Login attempt for user: {form_data.username}")  # ログ出力
    user_dict = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    # logger.info(f"user_dict: {user_dict}")  # ログ出力
    # if user_dict:
    #     logger.info(f"Password: {form_data.password} {user_dict.password}")  # ログ出力
    if not user_dict or not Hash().verify_password(form_data.password, user_dict.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    # HTTPOnly属性を付与してCookieに保存
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)) -> TokenData:
    '''
    ユーザー情報取得
    :param token: str: トークン
    :return: TokenData: ユーザー情報
    '''
    token_data = verify_token(token)
    return {"username": token_data.username}

@app.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)) -> dict:
    '''
    ログアウト
    :param token: str: トークン
    :return: dict: レスポンス
    '''
    # トークンをブラックリストに追加
    redis.set(token, "revoked", ex=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    return {"msg": "Successfully logged out"}