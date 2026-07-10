import os
import sys
from pathlib import Path

WORKSPACE: str = "WORKSPACE"
"""Variable for setting a common directories root"""

from smartdirs.base import SmartDirsBase
from smartdirs.flavor.macos import SmartDirsMacOS
from smartdirs.flavor.unix import SmartDirsUnix
from smartdirs.flavor.windows import SmartDirsWindows
from smartdirs.flavor.workspace import SmartDirsWorkspace

# Global dispatch branch on flavors
if os.environ.get(WORKSPACE, None):
    SmartDirs = SmartDirsWorkspace

elif os.name == "posix":
    SmartDirs = SmartDirsUnix

elif sys.platform.startswith("darwin"):
    SmartDirs = SmartDirsMacOS

elif sys.platform.startswith("win"):
    SmartDirs = SmartDirsWindows

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
