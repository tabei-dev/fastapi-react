from app.domain.value_objects.username import Username
from app.domain.value_objects.password import Password
from app.domain.value_objects.token_type import TokenType
from app.domain.value_objects.token import Token, create_token

class Auth:
    username: Username
    password: Password
    token_type: TokenType
    token: Token

    # def __init__(self, username: str, plain_password: str, hashed_password: str):
    #     self.username = Username(username)
    #     self.password = Password(plain_password, hashed_password)
    #     self.token_type = TokenType()
    #     self.token = create_token(username)
    def __init__(self, username: Username, password: Password, token_type: TokenType, token: Token):
        self.username = username
        self.password = password
        self.token_type = token_type
        self.token = token
