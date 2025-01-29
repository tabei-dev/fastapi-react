class ValidationError(Exception):
    '''
    バリデーションエラークラス
    '''
    def __init__(self, message: str, fieldname: str | None = None):
        '''
        コンストラクタ
        :param message: str: エラーメッセージ
        :param fieldname: str: 項目名
        '''
        self.message = message
        self.fieldname = fieldname

        super().__init__(message)