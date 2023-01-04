import importlib
import os
import sys
from types import ModuleType
from typing import Union

from rich import print
from rich.traceback import install


def _resolve_module(module: Union[str, ModuleType]) -> ModuleType:
    if type(module) is str:
        try:
            return importlib.import_module(module)
        except ImportError:
            print(
                f"\[rich-tracebacks] [bold yellow]Warning:[/] Treating [bold]{module}[/] as a path because "
                f"no module with that name was found."
            )

    return module


def _pycharm_override():
    try:
        pydevd = importlib.import_module("_pydevd_bundle.pydevd_breakpoints")
    except ImportError:
        return
    else:
        pydevd._fallback_excepthook = sys.excepthook


if os.getenv("RICH_TRACEBACKS"):
    try:
        from rt_config import config
    except ImportError:
        config = {}

    config["suppress"] = [
        _resolve_module(module) for module in config.get("suppress", [])
    ]

    install(**config)

    if os.getenv("RICH_TRACEBACKS_PYCHARM"):
        _pycharm_override()
