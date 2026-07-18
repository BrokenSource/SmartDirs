import os
from pathlib import Path

from pydantic import computed_field

from smartdirs.base import SmartDirsBase


class SmartDirsUnix(SmartDirsBase):

    # ------------------------------------------------------------------------ #

    @computed_field
    @property
    def user_home(self) -> Path:
        return Path.home()

    @computed_field
    @property
    def base_cache(self) -> Path:
        return Path(os.environ.get(
            key="XDG_CACHE_HOME",
            default=Path.home().joinpath(".cache"),
        ))

    @computed_field
    @property
    def base_config(self) -> Path:
        return Path(os.environ.get(
            key="XDG_CONFIG_HOME",
            default=Path.home().joinpath(".config"),
        ))

    @computed_field
    @property
    def base_data(self) -> Path:
        return Path(os.environ.get(
            key="XDG_DATA_HOME",
            default=Path.home().joinpath(".local", "share"),
        ))

    @computed_field
    @property
    def base_runtime(self) -> Path:
        return Path(os.environ.get(
            key="XDG_RUNTIME_DIR",
            default=Path("/run/user", str(os.getuid()))
        ))

    # ------------------------------------------------------------------------ #

    @computed_field
    @property
    def app_subdir(self) -> Path:
        return Path(self.app)
