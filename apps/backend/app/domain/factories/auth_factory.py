from app.domain.factories.token_factory import create_token_by_username
from app.domain.value_objects.auth import Auth
from app.domain.value_objects.username import Username
from app.domain.value_objects.hashed_password import HashedPassword
from app.domain.value_objects.token_type import TokenType

def create_auth(username: str, plain_password: str, hashed_password: str) -> Auth:
    _username = Username(username)
    _hashed_password = HashedPassword(plain_password, hashed_password)
    _token_type = TokenType()
    _token = create_token_by_username(username)

    return Auth(_username, _hashed_password, _token_type, _token)
