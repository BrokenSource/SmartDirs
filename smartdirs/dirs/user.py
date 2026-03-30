import os
from pathlib import Path
from typing import TYPE_CHECKING

from attrs import define
from smartdirs.platform import Platform

if TYPE_CHECKING:
    from smartdirs import SmartDirs

@define
class UserDirs:
    base: SmartDirs

    @property
    def data(self) -> Path:
        if self.base.platform == Platform.Linux:
            return Path.home().joinpath(
                os.getenv("XDG_DATA_HOME", ".local/share"),
                self.base.author,
                self.base.name,
            )
        raise NotImplementedError

    @property
    def downloads(self) -> Path:
        if self.base.platform == Platform.Linux:
            return Path.home().joinpath(
                os.getenv("XDG_DOWNLOAD_DIR", "Downloads")
            )
        elif self.base.platform == Platform.MacOS:
            return Path.home().joinpath("Downloads")
        raise NotImplementedError

    @property
    def runtime(self) -> Path:
        if self.base.platform == Platform.Linux:
            return Path("/run/user").joinpath(
                str(os.getuid()),
                self.base.author,
                self.base.name,
            )
        raise NotImplementedError