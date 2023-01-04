# rich-tracebacks

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rich-tracebacks?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/rich-tracebacks)
[![PyPI](https://img.shields.io/pypi/v/rich-tracebacks?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/rich-tracebacks)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/rich-tracebacks?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/rich-tracebacks/releases)
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

Set the `RICH_TRACEBACKS` environment variable. The value of the variable doesn't matter, but we'll use `1` as an
example.

```bash
export RICH_TRACEBACKS=1
```

That's it. Rich's traceback handler will be automatically installed each time you run your program.

### Disabling

Unset the `RICH_TRACEBACKS` environment variable.

```bash
unset RICH_TRACEBACKS
```

### Configuration

You can configure the traceback handler with
its [supported options](https://rich.readthedocs.io/en/stable/reference/traceback.html#rich.traceback.install)
by creating an `rt_config.py` file at your project's root. The file should contain a dictionary named `config`
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

Options that are not defined in `rt_config.py` will fall back to their default values. If `rt_config.py`
does not exist, all options will fall back to their default values.

#### A note on the `suppress` option

Rich's traceback handler supports a `suppress` option to which you can pass an iterable of modules and paths to be
excluded from tracebacks. To suppress a module, you would normally need to import the module and then pass the
module object to the `suppress` option. For example:

```python
import loctocat
from rich.traceback import install

install(suppress=[loctocat])
```

With rich-tracebacks, you also have the option of simply passing the module's name as a string. For example:

```python
# rt_config.py

config = {
    "suppress": ["loctocat"],
    ...
}
```

rich-tracebacks will do the work of importing the module for you and passing the module object to Rich.
Names it can't import will be passed to Rich as literal strings, which will in turn treat them as paths.

## FAQ

### Q: I use PyCharm and rich-tracebacks doesn't seem to be working if my program calls `sys.excepthook` while I'm using the debugger, please help.

A: Congratulations on encountering this ridiculously niche isssue. Setting the `RICH_TRACEBACKS_PYCHARM` environment
variable in the relevant run configuration will apply a very much experimental fix for this issue. If it doesn't work,
[open an issue](https://github.com/celsiusnarhwal/rich-tracebacks/issues/new) and I will try to help you as best I can.

## License

rich-tracebacks is licensed under
the [MIT License](https://github.com/celsiusnarhwal/rich-tracebacks/blob/main/LICENSE.md).


