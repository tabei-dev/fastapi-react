import dataclasses
import jwt
from app.domain.value_objects.username import Username
from app.helpers.settings import settings

__ALGORITHM = "HS256"

@dataclasses.dataclass(frozen=True)
class Token:
    access_token: str

    def __str__(self) -> str:
        return self.access_token

    def fetch_username(self) -> Username:
        try:
            payload = jwt.decode(self.access_token, settings.SECRET_KEY, algorithms=[__ALGORITHM])
            username: str = payload.get("sub")
            if username:
                return Username(username)
        except jwt.PyJWTError:
            pass

        raise Exception("Invalid token")
