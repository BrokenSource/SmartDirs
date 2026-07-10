import tempfile
from abc import ABC, abstractmethod
from collections.abc import Callable
from pathlib import Path

from pydantic import BaseModel, Field, model_serializer


class UserOptions(BaseModel):
    ...


class SmartDirsBase(BaseModel, ABC):
    """Nice platform directories and utilities class"""

    package: Path
    """Path to the package root"""

    app: str = Field()
    """Application name for directories"""

    org: str = Field()
    """Author or vendor name for directories"""

    @property
    def repository(self) -> Path:
        """Path to the repository root"""
        return self.package.parent

    @property
    def tempdir(self) -> Path:
        return Path(tempfile.gettempdir())

    # ------------------------------------------------------------------------ #

    @property
    def resources(self) -> Path:
        """Path to the resources directory"""
        return self.package.joinpath("resources")

    # ------------------------------------------------------------------------ #

    @abstractmethod
    def base_home(self) -> Path:
        """
        | Where     | Value                | Example            |
        | :-------- | :------------------- | :----------------- |
        | Linux     | `$HOME`              | `/home/alice`      |
        | macOS     | `$HOME`              | `/Users/Alice`     |
        | Windows   | `{FOLDERID_Profile}` | `C:\\Users\\Alice` |
        | Workspace | `$WORKSPACE`         | `/workspace`       |
        """

    @abstractmethod
    def base_cache(self) -> Path:
        """
        | Where     | Value                                  | Example                            |
        | :-------- | :------------------------------------- | :--------------------------------- |
        | Linux     | `$XDG_CACHE_HOME` or `$HOME/.cache`    | `/home/alice/.config`              |
        | macOS     | `$HOME/Library/Caches`                 | `/Users/Alice/Library/Caches`      |
        | Windows   | `{FOLDERID_LocalAppData}`              | `C:\\Users\\Alice\\AppData\\Local` |
        | Workspace | `$WORKSPACE/base/cache`                | `/workspace/base/cache`            |
        """

    @abstractmethod
    def base_config(self) -> Path:
        """
        | Where     | Value                                  | Example                            |
        | :-------- | :------------------------------------- | :--------------------------------- |
        | Linux     | `$XDG_CACHE_HOME` or `$HOME/.cache`    | `/home/alice/.config`              |
        | macOS     | `$HOME/Library/Caches`                 | `/Users/Alice/Library/Caches`      |
        | Windows   | `{FOLDERID_LocalAppData}`              | `C:\\Users\\Alice\\AppData\\Local` |
        | Workspace | `$WORKSPACE/base/cache`                | `/workspace/base/cache`            |
        """

    @abstractmethod
    def base_data(self) -> Path:
        """
        Persistent data storage for applications.
        | Where     | Value                                    | Example                                    |
        | :-------- | :--------------------------------------- | :----------------------------------------- |
        | Linux     | `$XDG_DATA_HOME` or `$HOME/.local/share` | `/home/alice/.local/share`                 |
        | macOS     | `$HOME/Library/Application Support`      | `/Users/Alice/Library/Application Support` |
        | Windows   | `{FOLDERID_RoamingAppData}`              | `C:\\Users\\Alice\\AppData\\Local`         |
        | Workspace | `$WORKSPACE/base/data`                   | `/workspace/base/data`                     |
        """

    @abstractmethod
    def base_runtime(self) -> Path:
        """
        Live application data that resets on reboot, similar to /tmp but only user-writable.
        | Where     | Value                                      | Example          |
        | :-------- | :----------------------------------------- | :--------------- |
        | Linux     | `$XDG_RUNTIME_DIR` or `/run/user/${id -u}` | `/run/user/1000` |
        | macOS     | `None`                                     | `None`           |
        | Windows   | `None`                                     | `None`           |
        | Workspace | Same for host platform                     | dynamic          |
        """

    # ------------------------------------------------------------------------ #

    @abstractmethod
    def app_subdir(self) -> Path:
        ...

    @abstractmethod
    def app_runtime(self) -> Path:
        """
        Live application data that resets on reboot, similar to /tmp but only user-writable.
        | Where     | Value                                      | Example          |
        | :-------- | :----------------------------------------- | :--------------- |
        | Linux     | `$XDG_RUNTIME_DIR` or `/run/user/${id -u}` | `/run/user/1000` |
        | macOS     | `None`                                     | `None`           |
        | Windows   | `None`                                     | `None`           |
        | Workspace | Same for host platform                     | dynamic          |
        """

    # ------------------------------------------------------------------------ #

    user: UserOptions = UserOptions()

    # ------------------------------------------------------------------------ #

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        data = handler(self)

        def export(*methods: Callable):
            return {get.__name__: get() for get in methods} # type: ignore

        data.update(export(
            self.base_home,
            self.base_cache,
            self.base_config,
            self.base_data,
            self.base_runtime,
            self.app_subdir,
            self.app_runtime,
        ))

        return data
