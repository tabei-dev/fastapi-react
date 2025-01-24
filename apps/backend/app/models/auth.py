from pydantic import BaseModel

class Auth(BaseModel):
    '''
    認証情報
    :param username: str: ユーザー名
    :param email: str: メールアドレス
    :param role_cls: str: 権限区分
    :param token_type: str: トークンの種類
    :param access_token: str: トークン
    '''
    username: str
    email: str
    role_cls: str
    token_type: str
    access_token: str
