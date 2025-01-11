# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# class HashUtil:
#     '''
#     ハッシュユーティリティ
#     '''

#     @staticmethod
#     def get_password_hash(password: str) -> str:
#         '''
#         パスワードのハッシュ化
#         :param password: str: ハッシュ化するパスワード
#         :return: str: ハッシュ化されたパスワード
#         '''
#         return pwd_context.hash(password)

#     @staticmethod
#     def verify_password(plain_password: str, hashed_password: str) -> bool:
#         '''
#         パスワードの検証
#         :param plain_password: str: 検証するパスワード
#         :param hashed_password: str: ハッシュ化されたパスワード
#         :return: bool: 検証結果
#         '''
#         return pwd_context.verify(plain_password, hashed_password)

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

class HashUtil:
    '''
    ハッシュユーティリティ
    '''

    @staticmethod
    def get_hashed_password(password: str) -> str:
        '''
        ハッシュ化したパスワードを取得します
        :param password: str: ハッシュ化するパスワード
        :return: str: ハッシュ化されたパスワード
        '''
        return ph.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        '''
        パスワードの検証
        :param plain_password: str: 検証するパスワード
        :param hashed_password: str: ハッシュ化されたパスワード
        :return: bool: 検証結果
        '''
        try:
            return ph.verify(hashed_password, plain_password)
        except VerifyMismatchError:
            return False