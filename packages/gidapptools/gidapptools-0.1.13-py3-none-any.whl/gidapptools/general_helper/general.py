"""
WiP.

Soon.
"""

# region [Imports]


from pathlib import Path
from typing import Any
import sys
from typing import Hashable, Iterable, Union
from gidapptools.general_helper.enums import MiscEnum
from logging import Logger, Manager
# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [Logging]


# endregion[Logging]

# region [Constants]

THIS_FILE_DIR = Path(__file__).parent.absolute()

# endregion[Constants]


def defaultable_list_pop(in_list: list, idx: int, default: Any = None) -> Any:
    if in_list is None:
        return default
    try:
        return in_list.pop(idx)
    except IndexError:
        return default


def dict_pop_fallback(in_dict: dict, keys: Union[Iterable[Hashable], Hashable], default: Any = None) -> Any:
    for key in keys:
        value = in_dict.pop(key, MiscEnum.NOT_FOUND)
        if value is not MiscEnum.NOT_FOUND:
            return value
    return default


def is_frozen() -> bool:
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')


def get_all_available_loggers(logger: Logger) -> tuple[str]:
    manager = logger.manager
    names = set(manager.loggerDict)
    return tuple(sorted(names, key=len))
# region[Main_Exec]


if __name__ == '__main__':
    pass

# endregion[Main_Exec]
