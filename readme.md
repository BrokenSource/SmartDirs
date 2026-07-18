> [!IMPORTANT]
> Work in progress, will roughly follow [`crates/directories`](https://crates.io/crates/directories), internal dogfooding for now.

<div align="center">
  <h1>SmartDirs</h1>
  <span>📂 System Directories and Utilities 📂</span>
  <br><br>
  <a href="https://pypi.org/project/smartdirs/"><img src="https://img.shields.io/pypi/v/smartdirs?label=PyPI&color=blue"></a>
  <a href="https://pypi.org/project/smartdirs/"><img src="https://img.shields.io/pypi/dw/smartdirs?label=%E2%86%93&color=blue"></a>
</div>

## 📦 Description

A modular platform directories package with conveniences:

- **Workspace**: Set a common root for all directories to isolate or avoid pollution
- **Resources**: Use the package root to tell resources directly, avoiding importlib
- **Pydantic**: Get a dict or json for all directories, simple cli for stdout print
- **Exports** `pathlib.Path` for a single import line in your package init 😉

## 📦 Usage

```python
# file: appname/__init__.py
from smartdirs import Path, SmartDirs

dirs = SmartDirs(
    pkg=Path(__file__).parent,
    app=str(__package__),
    org="author",
    url="com",
)
```

```python
# file: appname/main.py
import appname

# Access paths
appname.dirs.user_data
appname.dirs.resources
```
