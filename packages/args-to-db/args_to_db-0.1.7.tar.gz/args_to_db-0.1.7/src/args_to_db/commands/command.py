from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class Command:
    args: List[str]
    dependencies: List[str] = field(default_factory=list)
    cores: int = 1

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Command):
            return False

        return (self.args == other.args) and \
               (self.dependencies == other.dependencies)

    def __repr__(self) -> str:
        return ' '.join(self.args)

    def __hash__(self) -> int:
        return hash((*self.args, *self.dependencies))  # type: ignore
