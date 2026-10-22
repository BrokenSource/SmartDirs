import os
from pathlib import Path
from typing import override

from pydantic import Field, computed_field

import smartdirs
from smartdirs import WORKSPACE
from smartdirs.base import SmartDirsBase


class SmartDirsWorkspace(SmartDirsBase):
    root: Path = Field(default_factory=lambda:
        Path(os.environ[WORKSPACE]))

    # ------------------------------------------------------------------------ #

    @computed_field
    @property
    @override
    def user_home(self) -> Path:
        return self.root

    @computed_field
    @property
    @override
    def base_cache(self) -> Path:
        return self.root.joinpath("base", "cache")

    @computed_field
    @property
    @override
    def base_config(self) -> Path:
        return self.root.joinpath("base", "config")

    @computed_field
    @property
    @override
    def base_data(self) -> Path:
        return self.root.joinpath("base", "data")

    @computed_field
    @property
    @override
    def base_runtime(self) -> Path:
        return smartdirs.SmartDirs.base_runtime(self)

    # ------------------------------------------------------------------------ #

    @computed_field
    @property
    @override
    def app_subdir(self) -> Path:
        return Path(self.app)
