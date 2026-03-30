from pathlib import Path

from attrs import Factory, define, field

from smartdirs.dirs.site import SiteDirs
from smartdirs.dirs.user import UserDirs
from smartdirs.platform import Platform


@define
class SmartDirs:
    """Nice platform directories and utilities class"""

    package: Path
    """
    Path to the editable local or site-packages python package

    Warn: Must send the importer's root init `__file__` global here!
    """

    name: str = field()
    """
    Application name for directories

    Tip: Send the importer's root init `__package__` global here!
    """

    author: str = field(default="")
    """Author or vendor name for directories"""

    user: UserDirs = Factory(UserDirs, takes_self=True)
    """Specific directories for the current user"""

    site: SiteDirs = Factory(SiteDirs, takes_self=True)
    """Shared across users or system-wide directories"""

    platform: Platform = Factory(Platform.host)

    def __attrs_post_init__(self):
        self.package = Path(self.package).parent

    @property
    def repo(self) -> Path:
        """Path to the repository root"""
        return self.package.parent

    @property
    def resources(self) -> Path:
        """Path to the resources directory"""
        return self.package.joinpath("resources")
