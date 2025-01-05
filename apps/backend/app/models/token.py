from pydantic import BaseModel

class Token(BaseModel):
    '''
    トークンのレスポンスモデル
    :param access_token: str: トークン
    :param token_type: str: トークンの種類
    '''
    access_token: str
    token_type: str