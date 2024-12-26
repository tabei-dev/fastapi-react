# import logging
import redis as Redis
import jwt
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from app.config.database import get_db
from app.config.settings import settings
from app.models.user import User
from app.utils.hash import Hash

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

app = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Redisに接続
redis = Redis.Redis(host='redis', port=settings.redis_port, db=0)

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(settings.access_token_expire_minutes)

class Token(BaseModel):
    '''
    トークンのレスポンスモデル
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    '''
    access_token: str
    token_type: str

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    '''
    トークンを生成する
    :param data: dict: ペイロード
    :param expires_delta: timedelta | None: 有効期限
    :return: str: トークン
    '''
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str) -> dict:
    '''
    トークンを検証する
    :param token: str: トークン
    :return: dict: ペイロード
    '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        # token_data = TokenData(username=username)
        token_data = {"username": username}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # トークンがブラックリストにあるか確認
    if redis.get(token):
        raise HTTPException(status_code=401, detail="Token has been revoked")

    return token_data

def authenticate_user(db: Session, username: str, password: str) -> User:
    '''
    ユーザーを認証する
    :param db: Session: DBセッション
    :param username: str: ユーザー名
    :param password: str: パスワード
    :return: User: ユーザー
    '''
    user = db.query(User).filter(User.username == username).first()
    if not user or not Hash().verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user

def create_user_token(username: str) -> str:
    '''
    ユーザーのトークンを生成する
    :param username: str: ユーザー名
    :return: str: トークン
    '''
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_access_token(data={"sub": username}, expires_delta=access_token_expires)

def set_access_token_cookie(response: Response, access_token: str) -> None:
    '''
    トークンをCookieにセットする
    :param response: Response: レスポンス
    :param access_token: str: トークン
    '''
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

'''▼▽▼ エンドポイント ▼▽▼'''

@app.post("/token", response_model=Token)
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
) -> dict:
    '''
    ログイン
    :param response: Response: レスポンス
    :param form_data: OAuth2PasswordRequestForm: フォームデータ
    :param db: Session: DBセッション
    :return: dict: トークン
    '''
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_user_token(user.username)
    set_access_token_cookie(response, access_token)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)) -> dict:
    '''
    ユーザー情報取得
    :param token: str: トークン
    :return: dict: ユーザー情報
    '''
    token_data = verify_token(token)
    return {"username": token_data["username"]}

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