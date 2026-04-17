<div align="center">
  <h1>SmartDirs</h1>
  <span>📂 System Directories and Utilities 📂</span>
  <br>
  <br>
    <a href="https://pypi.org/project/smartdirs/"><img src="https://img.shields.io/pypi/v/smartdirs?label=PyPI&color=blue"></a>
    <a href="https://pypi.org/project/smartdirs/"><img src="https://img.shields.io/pypi/dw/smartdirs?label=%E2%86%93&color=blue"></a>
  <br>
</div>

# Description

Work in progress, will roughly follow https://crates.io/crates/directories, internal dogfooding for now.

Usage:

```python
# file: appname/__init__.py
from smartdirs import Path, SmartDirs

dirs = SmartDirs(
    package=Path(__file__),
    name=str(__package__),
)
```

```python
# file: appname/main.py
import appname

# Access paths
appname.dirs.user.data
appname.dirs.resources
```
