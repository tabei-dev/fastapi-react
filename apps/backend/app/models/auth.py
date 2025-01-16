from pydantic import BaseModel

class Auth(BaseModel):
    '''
    認証用レスポンスモデル
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    :param username: str: ユーザ名
    :param role_cls: str: 権限区分
    '''
    access_token: str
    token_type: str
    username: str
    role_cls: str