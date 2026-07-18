import os
import sys
from pathlib import Path

WORKSPACE: str = "WORKSPACE"
"""Variable for setting a common directories root"""

# Warn: Use base class for isinstance() checks!
from smartdirs.base import SmartDirsBase

# Global dispatch branch on flavors
from smartdirs.flavor.darwin import SmartDirsDarwin
from smartdirs.flavor.unix import SmartDirsUnix
from smartdirs.flavor.windows import SmartDirsWindows
from smartdirs.flavor.workspace import SmartDirsWorkspace

if (WORKSPACE in os.environ):
    SmartDirs = SmartDirsWorkspace

elif os.name == "posix":
    SmartDirs = SmartDirsUnix

elif sys.platform.startswith("win"):
    SmartDirs = SmartDirsWindows

elif sys.platform.startswith("darwin"):
    SmartDirs = SmartDirsDarwin

else:
    raise NotImplementedError((
        "Unknown platform for exporting a SmartDirs class"
    ))

dirs = SmartDirs(
    pkg=Path(__file__).parent,
    app=str(__package__),
    org="tremeschin",
    url="com",
)
"""A main SmartDirs instance so you can get static/base directories"""
