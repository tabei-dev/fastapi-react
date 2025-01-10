class ValidationError(Exception):
    '''
    バリデーションエラークラス
    '''
    def __init__(self, err_msg: str, fieldname: str = None):
        '''
        コンストラクタ
        :param err_msg: str: エラーメッセージ
        :param fieldname: str: 項目名
        '''
        self.err_msg = err_msg
        self.fieldname = fieldname
        super().__init__(err_msg)