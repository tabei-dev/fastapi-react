from pusslib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#
# パスワードのハッシュ化と検証を行うクラス
#
class Hash():
    #
    # パスワードのハッシュ化
    #
    # @param password ハッシュ化するパスワード
    # @return ハッシュ化されたパスワード
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    #
    # パスワードの検証
    #
    # @param plain_password 検証するパスワード
    # @param hashed_password ハッシュ化されたパスワード
    # @return 検証結果
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)