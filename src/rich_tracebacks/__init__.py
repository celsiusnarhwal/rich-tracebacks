import os

from rich.traceback import install

if os.getenv("RICH_TRACEBACKS"):
    try:
        from rt_config import config
    except ImportError:
        config = {}

    install(**config)
