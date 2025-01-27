from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.helpers.database import get_database
from app.errors.validation_error import ValidationError
from app.models.auth import Auth
# from app.services.auth_service import auth_service
from app.usecases.auth_usecase import authenticate, verify_token, revoke_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login", response_model=Auth)
async def login(
        response: Response,
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_database)
    ) -> Auth:
    '''
    ログイン
    :param response: Response: レスポンス
    :param form_data: OAuth2PasswordRequestForm: フォームデータ
    :param db: Session: DBセッション
    :return: Auth: 認証情報
    '''
    try:
        auth = authenticate(db, form_data.username, form_data.password)
    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail={
                "fieldname": e.fieldname,
                "message": e.message,
            }
        )

    # トークンをCookieにセット
    response.set_cookie(key="access_token", value=f"Bearer {auth.access_token}", httponly=True)

    return auth

# @router.get("/users/me")
# async def read_users_me(token: str = Depends(oauth2_scheme)) -> dict[str, str]:
#     '''
#     ユーザー情報取得
#     :param token: str: トークン
#     :return: dict: レスポンス（ユーザー情報）
#     '''
#     username = verify_token(token)

#     return {"username": username}

@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)) -> dict[str, str]:
    '''
    ログアウト
    :param token: str: トークン
    :return: dict: レスポンス
    '''
    revoke_token(token)

    return {"msg": "Successfully logged out"}