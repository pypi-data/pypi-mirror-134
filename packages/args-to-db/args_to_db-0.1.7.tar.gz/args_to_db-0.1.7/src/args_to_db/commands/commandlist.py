from dataclasses import dataclass
from typing import Any, List

from args_to_db.commands.command import Command


@dataclass
class CommandList:

    commands: List[Command]

    @classmethod
    def empty(cls):
        return cls([])

    def __add__(self, other):
        assert isinstance(other, CommandList)
        # TODO type checking not as assert?

        if self == CommandList.empty():
            return CommandList(other.commands.copy())

        if other == CommandList.empty():
            return CommandList(self.commands.copy())

        commands = []
        for s_cmds in self.commands:
            for o_cmds in other.commands:
                commands += [Command(s_cmds.args + o_cmds.args)]

        return CommandList(commands)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CommandList):
            return False

        return self.commands == other.commands

    def __len__(self) -> int:
        return len(self.commands)
