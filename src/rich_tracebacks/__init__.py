import importlib
import os
from pathlib import Path
from types import ModuleType
from typing import Union

from rich import print
from rich.traceback import install


def _resolve_module(module: Union[str, ModuleType]) -> ModuleType:
    if type(module) is str:
        try:
            return importlib.import_module(module)
        except ImportError:
            if not Path(module).exists():
                print(
                    f"\[rich-tracebacks] [bold yellow]Warning:[/] Treating [bold]{module}[/] as a path because "
                    f"no module with that name was found."
                )

    return module


if os.getenv("RICH_TRACEBACKS"):
    try:
        from rt_config import config
    except ImportError:
        config = {}

    config["suppress"] = [
        _resolve_module(module) for module in config.get("suppress", [])
    ]

    install(**config)
