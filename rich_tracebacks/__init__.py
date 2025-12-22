import importlib
import os
import sys

from rich.traceback import install


def noop(*_, **__):
    pass


if os.getenv("RICH_TRACEBACKS"):
    try:
        from rt_config import config
    except ImportError:
        config = {}

    install(**config)

    if os.getenv("RICH_TRACEBACKS_PYCHARM"):
        try:
            pydevd = importlib.import_module("pydevd")
            breakpoints = importlib.import_module("_pydevd_bundle.pydevd_breakpoints")
        except ImportError:
            pass
        else:
            config["suppress"] = [pydevd] + [
                module for module in config.get("suppress", [])
            ]

            install(**config)

            breakpoints.dummy_excepthook = sys.excepthook
            breakpoints.original_excepthook = noop
