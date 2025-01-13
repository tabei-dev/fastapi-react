from pydantic import BaseModel

class Error(BaseModel):
    '''
    エラーのレスポンスモデル
    :param field_name: str: 項目名
    :param error_message: str: エラーメッセージ
    '''
    field_name: str
    error_message: str