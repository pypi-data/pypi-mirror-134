from dataclasses import dataclass
from typing import Dict, List
from pandas import DataFrame

from args_to_db.commands.command import Command
from args_to_db.control.state import State


@dataclass
class RunResult:
    states: Dict[Command, State]
    data: DataFrame

    def write_data(self, path: str) -> None:
        self.data.to_pickle(path)
        # if debug
        # self.data.to_csv(f'{path}.csv')

    def states_filtered(self, state: State) -> List[Command]:
        return [cmd for cmd, st in self.states.items() if st == state]
