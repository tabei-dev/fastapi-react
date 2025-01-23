from sqlalchemy.orm import Session
from app.errors.validation_error import ValidationError
from app.managers.token_manager import token_manager
from app.models.auth import Auth, create_auth
from app.models.user import User
from app.services.message_service import message_service

class AuthService:
    '''
    認証サービスクラス
    '''
    def authenticate(self, db: Session, username: str, password: str) -> Auth:
        '''
        ユーザー認証し、成功したら認証情報を生成してこれを返します
        :param _db: Session: DBセッション
        :param username: str: ユーザー名
        :param password: str: パスワード
        :return: Auth: 認証情報
        :raise ValidationError: ユーザーが見つからない場合
        :raise ValidationError: パスワードが一致しない場合
        '''
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise ValidationError(message_service.get_message('4001'), 'username')
        
        if not user.verify_password(password):
            raise ValidationError(message_service.get_message('4002'), 'password')

        access_token = token_manager.create_access_token(username)

        auth = create_auth(
            access_token,
            token_manager.TOKEN_TYPE,
            user.username,
            user.email,
            user.role_cls,
        )

        return auth

    def verify_token(self, token: str) -> str:
        '''
        トークンを検証します
        検証に成功した場合、ユーザー名を返します
        :param token: str: トークン
        :return: str: ユーザー名
        :raise ValueError: トークンが不正な場合
        :raise ValueError: トークンがブラックリストにある場合
        '''
        username = token_manager.verify_token(token)
        return username

    def revoke_token(self, token: str) -> None:
        '''
        トークンを削除します
        :param token: str: トークン
        '''
        # トークンをブラックリストに追加
        token_manager.add_token_to_blacklist(token)

auth_service = AuthService()