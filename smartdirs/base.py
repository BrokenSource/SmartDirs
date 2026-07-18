import contextlib
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generator, Optional

from pydantic import BaseModel, Field, computed_field


class SmartDirsBase(BaseModel, ABC):
    """
    Nice platform directories and utilities class

    - **App**: Application directories
    - **Base**: Hidden user directories
    - **User**: Visible user-facing directories
    - **Site**: System directories
    """

    pkg: Path
    """Path to the package root"""

    app: str = Field()
    """Application name for directories"""

    org: str = Field()
    """Author or vendor name for directories"""

    url: Optional[str] = None
    """Reverse domain name"""

    @property
    @computed_field
    def repository(self) -> Path:
        """Path to the repository root"""
        return self.pkg.parent

    @property
    @computed_field
    def tempdir(self) -> Path:
        return Path(tempfile.gettempdir())

    # ------------------------------------------------------------------------ #

    @property
    @computed_field
    def resources(self) -> Path:
        """Path to the resources directory"""
        return self.pkg.joinpath("resources")

    # ------------------------------------------------------------------------ #

    @property
    @abstractmethod
    def user_home(self) -> Path:
        """
        | Where     | Value                | Example            |
        | :-------- | :------------------- | :----------------- |
        | Linux     | `$HOME`              | `/home/alice`      |
        | macOS     | `$HOME`              | `/Users/Alice`     |
        | Windows   | `{FOLDERID_Profile}` | `C:\\Users\\Alice` |
        | Workspace | `$WORKSPACE`         | `/workspace`       |
        """

    @property
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

    @property
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

    @property
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

    @property
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

    @property
    @abstractmethod
    def app_subdir(self) -> Path:
        ...

    @property
    @computed_field
    def app_cache(self) -> Path:
        return self.base_cache.joinpath(self.app_subdir)

    @property
    @computed_field
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
        return self.base_runtime.joinpath(self.app_subdir)

    @contextlib.contextmanager
    def app_tempdir(self) -> Generator[Path, None, None]:
        with tempfile.TemporaryDirectory(
            prefix=self.app,
        ) as directory:
            yield Path(directory)

    # ------------------------------------------------------------------------ #
