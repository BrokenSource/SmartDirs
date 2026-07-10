import os
from pathlib import Path

from pydantic import BaseModel, Field, computed_field

from smartdirs.platform import Platform


class UserOptions(BaseModel):
    ...

class SmartDirs(BaseModel):
    """Nice platform directories and utilities class"""

    package: Path
    """Path to the package root"""

    name: str = Field()
    """Application name for directories"""

    author: str = Field("")
    """Author or vendor name for directories"""

    platform: Platform = Field(default_factory=Platform.host)

    # ------------------------------------------------------------------------ #

    @computed_field
    @property
    def resources(self) -> Path:
        """Path to the resources directory"""
        return self.package.joinpath("resources")

    @property
    def repository(self) -> Path:
        """Path to the repository root"""
        return self.package.parent

    # ------------------------------------------------------------------------ #

    user: UserOptions = UserOptions()

    @computed_field
    @property
    def user_cache(self) -> Path:
        if self.platform == Platform.Linux:
            return Path.home().joinpath(
                os.getenv("XDG_DATA_HOME", ".local/share"),
                self.author,
                self.name,
            )
        raise NotImplementedError

    @computed_field
    @property
    def user_downloads(self) -> Path:
        if self.platform == Platform.Linux:
            return Path.home().joinpath(
                os.getenv("XDG_DOWNLOAD_DIR", "Downloads")
            )
        elif self.platform == Platform.MacOS:
            return Path.home().joinpath("Downloads")
        raise NotImplementedError

    # ------------------------------------------------------------------------ #

