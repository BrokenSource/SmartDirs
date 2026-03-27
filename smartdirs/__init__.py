from pathlib import Path
from typing import Optional

from attrs import define


@define
class SmartDirs:

    package: Path
    """
    Path to the local or site-dirs python package

    Tip: Send the importer's `__file__` global here!
    """

    name: str
    """
    Application name for directories

    Tip: Send the importer's `__package__` global
    """

    author: str
    """Author or vendor name for directories"""

    version: Optional[str] = None

    def __attrs_post_init__(self):
        self.package = Path(self.package)

    @property
    def resources(self) -> Path:
        """Path to the resources directory"""
        return self.package.joinpath("resources")
