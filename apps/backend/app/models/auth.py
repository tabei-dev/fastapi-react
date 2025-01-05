from pydantic import BaseModel

class Auth(BaseModel):
    '''
    認証情報
    :param username: str: ユーザ名
    :param password: str: パスワード
    '''
    username: str
    password: str