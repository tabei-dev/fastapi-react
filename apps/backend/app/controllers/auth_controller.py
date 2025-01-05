from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.token import Token
from app.services.auth_service import auth_service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login", response_model=Token)
async def login(
        response: Response,
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
    ) -> dict[str, str]:
    '''
    ログイン
    :param response: Response: レスポンス
    :param form_data: OAuth2PasswordRequestForm: フォームデータ
    :param db: Session: DBセッション
    :return: dict: レスポンス（トークン情報）
    '''
    try:
        access_token = auth_service.authenticate(db, form_data.username, form_data.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # トークンをCookieにセット
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)) -> dict[str, str]:
    '''
    ユーザー情報取得
    :param token: str: トークン
    :return: dict: レスポンス（ユーザー情報）
    '''
    try:
        username = auth_service.verify_token(token)
    except ValueError as e:
        logger.debug(f"エラー: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    return {"username": username}

@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)) -> dict[str, str]:
    '''
    ログアウト
    :param token: str: トークン
    :return: dict: レスポンス
    '''
    # トークンをブラックリストに追加
    auth_service.revoke_token(token)

    return {"msg": "Successfully logged out"}