from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel, Field, computed_field


class UserOptions(BaseModel):
    ...


class SmartDirsBase(ABC, BaseModel):
    """Nice platform directories and utilities class"""

    package: Path
    """Path to the package root"""

    name: str = Field()
    """Application name for directories"""

    vendor: str = Field()
    """Author or vendor name for directories"""

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

    @computed_field
    @abstractmethod
    def base_home(self) -> Path:
        """
        Path to the user's home directory
        | Where     | Value              | Example          |
        | :-------- | :----------------- | :--------------- |
        | Linux     | $HOME              | /home/alice      |
        | macOS     | $HOME              | /Users/Alice     |
        | Windows   | {FOLDERID_Profile} | C:\\Users\\Alice |
        | Workspace | $WORKSPACE         | -                |
        """

    @computed_field
    @abstractmethod
    def base_cache(self) -> Path:
        """
        - Linux: $XDG_CACHE_HOME or $HOME/.cache
        - macOS: $HOME/Library/Caches
        - MsWin: {FOLDERID_LocalAppData}
        """

    @computed_field
    @abstractmethod
    def base_config(self) -> Path:
        """
        - Linux: $XDG_CONFIG_HOME or $HOME/.config
        - macOS: $HOME/Library/Application Support
        - MsWin: {FOLDERID_RoamingAppData}
        """

    # ------------------------------------------------------------------------ #

    user: UserOptions = UserOptions()
