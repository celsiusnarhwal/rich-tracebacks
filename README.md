# rich-tracebacks

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rich-tracebacks?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/rich-tracebacks)
[![PyPI](https://img.shields.io/pypi/v/rich-tracebacks?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/rich-tracebacks)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/rich-tracebacks?logo=github&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/rich-tracebacks/releases)
[![PyPI - License](https://img.shields.io/pypi/l/rich-tracebacks?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/rich-tracebacks/blob/main/LICENSE)

rich-tracebacks automates the installation
of [Rich's traceback handler](https://rich.readthedocs.io/en/stable/traceback.html#traceback-handler) in Python
programs. Compared to Rich's
own [sanctioned method](https://rich.readthedocs.io/en/stable/traceback.html#automatic-traceback-handler)
of automatically installing its traceback handler, rich-tracebacks is markedly simpler and agnostic to your virtual
environment.

## Installation

```bash
pip install rich-tracebacks
```

## Usage

### Enabling

Set the `RICH_TRACEBACKS` environment variable to `1`.

```bash
export RICH_TRACEBACKS=1
```

That's it.

### Disabling

Set the `RICH_TRACEBACKS` environment variable to `0`.

```bash
export RICH_TRACEBACKS=0
```

Alternatively, you can unset the variable entirely.

```bash
unset RICH_TRACEBACKS
```

### Configuration

You can configure the traceback handler with
its [supported options](https://rich.readthedocs.io/en/stable/reference/traceback.html#rich.traceback.install)
by creating a `rt_config.py` file at your project's root. The file should contain a dictionary named `config`
that maps option names to their intended values. For example:

```python
# rt_config.py

config = {
    "show_locals": True,
    "width": 120,
    "theme": "monokai",
    ...
}
```

Of special note is the `console` option, which takes
a [Rich Console](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.Console) object. To use this
option, you must import the `Console` class in your `rt_config.py` file. For example:

```python
# rt_config.py

from rich.console import Console

config = {
    "console": Console(file=open("traceback.log", "w")),
    ...
}
```

Options that are not defined in `rt_config.py` will fall back to their default values. If `rt_config.py`
does not exist, all options will fall back to their default values.


