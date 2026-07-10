from pathlib import Path

from smartdirs.base import SmartDirsBase


class SmartDirsDarwin(SmartDirsBase):
    ...

    def app_subdir(self) -> Path:
        parts = filter(None, (self.url, self.org, self.app))
        return Path('.'.join(parts))
