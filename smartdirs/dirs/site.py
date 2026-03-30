from typing import TYPE_CHECKING

from attrs import define

if TYPE_CHECKING:
    from smartdirs import SmartDirs


@define
class SiteDirs:
    base: SmartDirs
