from dataclasses import dataclass
from app.domain.value_objects.username import Username
from app.domain.value_objects.hashed_password import HashedPassword
from app.domain.value_objects.token_type import TokenType
from app.domain.value_objects.token import Token

@dataclass(frozen=True)
class Auth:
    username: Username
    hashed_password: HashedPassword
    token_type: TokenType
    token: Token
