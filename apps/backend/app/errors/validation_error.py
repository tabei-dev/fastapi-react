from app.models.error import Error

class ValidationError(Exception):
    '''
    バリデーションエラークラス
    '''
    def __init__(self, error_massage: str, field_name: str | None = None):
        '''
        コンストラクタ
        :param error_massage: str: エラーメッセージ
        :param field_name: str: 項目名
        '''
        # self.error_massage = error_massage
        # self.field_name = field_name
        self.error: Error = {
            'error_massage': error_massage,
            'field_name': field_name
        }
        super().__init__(error_massage)