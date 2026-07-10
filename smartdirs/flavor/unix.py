import os
from pathlib import Path

from smartdirs.base import SmartDirsBase


class SmartDirsUnix(SmartDirsBase):

    # ------------------------------------------------------------------------ #

    def base_home(self) -> Path:
        return Path.home()

    def base_cache(self) -> Path:
        return Path(os.environ.get(
            key="XDG_CACHE_HOME",
            default=Path.home().joinpath(".cache"),
        ))

    def base_config(self) -> Path:
        return Path(os.environ.get(
            key="XDG_CONFIG_HOME",
            default=Path.home().joinpath(".config"),
        ))

    def base_data(self) -> Path:
        return Path(os.environ.get(
            key="XDG_DATA_HOME",
            default=Path.home().joinpath(".local", "share"),
        ))

    def base_runtime(self) -> Path:
        return Path(os.environ.get(
            key="XDG_RUNTIME_DIR",
            default=Path("/run/user", str(os.getuid()))
        ))

    # ------------------------------------------------------------------------ #

    def app_subdir(self) -> Path:
        return Path(self.app)

    def app_runtime(self) -> Path:
        return self.base_runtime().joinpath(self.app_subdir())
