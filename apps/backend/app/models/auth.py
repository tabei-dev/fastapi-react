from pydantic import BaseModel

class Auth(BaseModel):
    '''
    認証情報
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    :param username: str: ユーザー名
    :param email: str: メールアドレス
    :param role_cls: str: 権限区分
    '''
    access_token: str
    token_type: str
    username: str
    email: str
    role_cls: str

def create_auth(access_token: str, token_type: str, username: str, email: str, role_cls: str) -> Auth:
    '''
    認証情報を生成します
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    :param username: str: ユーザー名
    :param email: str: メールアドレス
    :param role_cls: str: 権限区分
    :return: Auth: 認証情報
    '''
    return Auth(
        access_token=access_token,
        token_type=token_type,
        username=username,
        email=email,
        role_cls=role_cls,
    )
