#
# パスワードのハッシュ化と検証
#
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    #
    # パスワードのハッシュ化
    #
    # @param password ハッシュ化するパスワード
    # @return ハッシュ化されたパスワード
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    #
    # パスワードの検証
    #
    # @param plain_password 検証するパスワード
    # @param hashed_password ハッシュ化されたパスワード
    # @return 検証結果
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
