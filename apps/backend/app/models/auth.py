from pydantic import BaseModel

class Auth(BaseModel):
    '''
    認証用レスポンスモデル
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