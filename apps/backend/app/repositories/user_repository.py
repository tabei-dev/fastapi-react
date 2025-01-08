from sqlalchemy.orm import Session
from app.models.user import User
from app.services.message_service import get_message
from app.utils.hash import HashUtil

class UserRepository:
    '''
    ユーザ情報リポジトリクラス
    '''

    def __init__(self, db: Session):
        '''
        コンストラクタ
        :param db: Session: DBセッション
        '''
        if not db:
            raise ValueError('DBセッションが設定されていません')

        self._db = db

    def authenticate(self, username: str, password: str) -> None:
        '''
        ユーザー認証を行う
        :param username: str: ユーザ名
        :param password: str: パスワード
        :raise ValueError: ユーザが見つからない場合
        :raise ValueError: パスワードが一致しない場合
        '''
        user = self._db.query(User).filter(User.username == username).first()
        if not user:
            raise ValueError(get_message(4001))

        # if not user.check_password(password):
        if not user or not HashUtil().verify_password(password, user.password):
            raise ValueError(get_message(4002))

    # def get_user(self, username: str) -> User:
    #     '''
    #     ユーザ情報を取得する
    #     :param username: str: ユーザ名
    #     :return: User: ユーザ情報
    #     '''
    #     return self._db.query(User).filter(User.username == username).first()