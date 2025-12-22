# Changelog[^1]

Notable changes to the rich-tracebacks will be documented here.

rich-tracebacks adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="2-0-0">2.0.0 — 2025-12-22</a>

### 🚨 Breaking Changes

- The `suppress` option in `rt_config.py` no longer supports passing modules by name. You now must import the modules
  you wish to suppress and pass the module objects to the `suppress` option.
- The PyCharm debug fix has been updated to work for PyCharm 2025.3 and later. It may work on earlier versions,
  but I can't guarantee it.

### Changed

- rich-tracebacks now supports Rich 12 and newer. Emphasis on "and newer"; it previously supported Rich 12 only.

## Older Releases

See [Releases](https://github.com/celsiusnarhwal/rich-tracebacks/releases).

[^1]: Format based on [Keep a Changelog](https://keepachangelog.com).
