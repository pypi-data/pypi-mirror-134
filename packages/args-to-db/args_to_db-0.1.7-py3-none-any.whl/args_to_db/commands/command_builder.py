import inspect
from typing import Any, Callable, Collection, Tuple

from args_to_db.commands.args import cmd
from args_to_db.commands.combine import combine
from args_to_db.commands.commandlist import CommandList


class _CommandBuilder:  # pylint: disable=too-few-public-methods

    def __init__(self,
                 func: Callable[[Any], Any],
                 prefix: CommandList = CommandList.empty(),
                 suffix: CommandList = CommandList.empty(),
                 flag_marker: str = '--') -> None:

        self._flag_marker = flag_marker
        self._func = func
        self._prefix = prefix
        self._suffix = suffix

        if not self._prefix:
            self._prefix = CommandList.empty()

        if not self._suffix:
            self._suffix = CommandList.empty()

    def _args_to_command(self, *args, **kwargs) -> CommandList:
        cmdlist = CommandList.empty()
        args_iter = iter(args)

        for name, sig in inspect.signature(self._func).parameters.items():

            # TODO: handle other kinds?!
            if sig.kind == inspect.Parameter.POSITIONAL_ONLY:
                pass
            elif sig.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
                # pylint: disable=protected-access
                if sig.default is inspect._empty:
                    cmdlist += cmd(str(next(args_iter)))
                else:
                    if name in kwargs:
                        cmdlist += cmd(f'{self._flag_marker}{name}',
                                       str(kwargs[name]))
                    else:
                        cmdlist += cmd(f'{self._flag_marker}{name}',
                                       str(next(args_iter)))
            elif sig.kind == inspect.Parameter.VAR_POSITIONAL:
                pass
            elif sig.kind == inspect.Parameter.KEYWORD_ONLY:
                pass
            elif sig.kind == inspect.Parameter.VAR_KEYWORD:
                pass

        return cmdlist

    def decorated_function(self, arg_tuples: Collection[Tuple]) -> CommandList:
        # TODO: add assert arg_tuples tuples have length of no. of args
        cmd_list = (self._args_to_command(*args) for args in arg_tuples)
        cmds = combine(*(_cmd for _cmd in cmd_list))
        return self._prefix + cmds + self._suffix


def command_builder(prefix: CommandList = None,
                    suffix: CommandList = None,
                    flag_marker: str = '--'):

    def decorator(func):
        builder = _CommandBuilder(func, prefix, suffix, flag_marker)
        return builder.decorated_function

    return decorator
