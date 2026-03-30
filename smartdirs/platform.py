import sys
from enum import Enum


# Fixme: How to flavors?
class Platform(Enum):
    Linux   = "linux"
    Windows = "windows"
    MacOS   = "macos"

    @classmethod
    def host(cls) -> 'Platform':
        if sys.platform.startswith("linux"):
            return cls.Linux
        elif sys.platform.startswith("win"):
            return cls.Windows
        elif sys.platform.startswith("darwin"):
            return cls.MacOS
        raise NotImplementedError
