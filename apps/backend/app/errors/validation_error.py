class ValidationError(Exception):
    '''
    バリデーションエラークラス
    '''
    def __init__(self, error_message: str, field_name: str | None = None):
        '''
        コンストラクタ
        :param error_massage: str: エラーメッセージ
        :param field_name: str: 項目名
        '''
        self.error_message = error_message
        self.field_name = field_name

        super().__init__(error_message)