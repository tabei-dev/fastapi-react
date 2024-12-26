from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashUtil:
    '''
    ハッシュユーティリティ
    '''

    @staticmethod
    def get_password_hash(password: str) -> str:
        '''
        パスワードのハッシュ化
        :param password: str: ハッシュ化するパスワード
        :return: str: ハッシュ化されたパスワード
        '''
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        '''
        パスワードの検証
        :param plain_password: str: 検証するパスワード
        :param hashed_password: str: ハッシュ化されたパスワード
        :return: bool: 検証結果
        '''
        return pwd_context.verify(plain_password, hashed_password)
