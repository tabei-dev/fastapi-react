import dataclasses

@dataclasses.dataclass(frozen=True)
class Username:
    username: str

    def __str__(self) -> str:
        return self.username
