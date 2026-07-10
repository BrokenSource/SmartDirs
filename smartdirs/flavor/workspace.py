import os
from pathlib import Path

from pydantic import Field

import smartdirs
from smartdirs import WORKSPACE
from smartdirs.base import SmartDirsBase


class SmartDirsWorkspace(SmartDirsBase):
    root: Path = Field(default_factory=lambda:
        Path(os.environ[WORKSPACE]))

    # ------------------------------------------------------------------------ #

    def base_home(self) -> Path:
        return self.root

    def base_cache(self) -> Path:
        return self.root.joinpath("base", "cache")

    def base_config(self) -> Path:
        return self.root.joinpath("base", "config")

    def base_data(self) -> Path:
        return self.root.joinpath("base", "data")

    def base_runtime(self) -> Path:
        return smartdirs.SmartDirs.base_runtime(self)

    # ------------------------------------------------------------------------ #

    def app_subdir(self) -> Path:
        return Path(self.app)
