from app.domain.value_objects.auth import Auth
from app.domain.value_objects.username import Username
from app.domain.value_objects.password import Password
from app.domain.value_objects.token_type import TokenType
from app.domain.value_objects.token import create_token

def create_auth(username: str, plain_password: str, hashed_password: str) -> Auth:
    _username = Username(username)
    _password = Password(plain_password, hashed_password)
    _token_type = TokenType()
    _token = create_token(username)

    return Auth(_username, _password, _token_type, _token)
