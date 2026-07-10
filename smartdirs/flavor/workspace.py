import os
from pathlib import Path

from pydantic import Field, computed_field

from smartdirs import WORKSPACE
from smartdirs.base import SmartDirsBase


class SmartDirsWorkspace(SmartDirsBase):
    root: Path = Field(default_factory=lambda:
        Path(os.environ[WORKSPACE])
    )

    @computed_field
    def base_home(self) -> Path:
        return self.root

    @computed_field
    def base_cache(self) -> Path:
        return self.root.joinpath("cache")

    @computed_field
    def base_config(self) -> Path:
        return self.root.joinpath("config")
