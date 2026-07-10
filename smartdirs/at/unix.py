import os
from pathlib import Path

from pydantic import computed_field

from smartdirs.base import SmartDirsBase


class SmartDirsUnix(SmartDirsBase):

    @computed_field
    def base_home(self) -> Path:
        return Path.home()

    @computed_field
    def base_cache(self) -> Path:
        return Path(os.environ.get(
            key="XDG_CACHE_HOME",
            default=Path.home().joinpath(".cache"),
        ))
