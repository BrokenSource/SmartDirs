import os
import sys
from pathlib import Path

WORKSPACE: str = "WORKSPACE"
"""Variable for setting a common directories root"""

# Global dispatch branch on flavors
if os.environ.get(WORKSPACE, None):
    from smartdirs.at.workspace import SmartDirsWorkspace as SmartDirs

elif os.name == "posix":
    from smartdirs.at.unix import SmartDirsUnix as SmartDirs

elif sys.platform.startswith("darwin"):
    from smartdirs.at.macos import SmartDirsMacOS as SmartDirs

elif sys.platform.startswith("win"):
    from smartdirs.at.windows import SmartDirsWindows as SmartDirs

else:
    raise NotImplementedError((
        "Unknown platform for exporting a SmartDirs class"
    ))

dirs = SmartDirs(
    package=Path(__file__).parent,
    name=str(__package__),
    vendor="brokensource",
)
"""A main SmartDirs instance so you can get static/base directories"""
