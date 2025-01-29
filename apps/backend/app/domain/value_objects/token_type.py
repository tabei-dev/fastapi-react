import dataclasses

@dataclasses.dataclass(frozen=True)
class TokenType:
    token_type = "Bearer"

    def __str__(self) -> str:
        return self.token_type
