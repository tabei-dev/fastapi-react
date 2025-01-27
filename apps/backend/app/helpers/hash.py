from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

__password_hasher = PasswordHasher()

def to_hashed_password(password: str) -> str:
    '''
    ハッシュ化したパスワードを取得します
    :param password: str: ハッシュ化するパスワード
    :return: str: ハッシュ化されたパスワード
    '''
    return __password_hasher.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''
    パスワードの検証
    :param plain_password: str: 検証するパスワード
    :param hashed_password: str: ハッシュ化されたパスワード
    :return: bool: 検証結果
    '''
    try:
        return __password_hasher.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False