from abc import ABCMeta
from pathlib import Path
from typing import override

from pydantic import computed_field

from smartdirs.base import SmartDirsBase


class SmartDirsDarwin(SmartDirsBase, metaclass=ABCMeta):

    @computed_field
    @property
    @override
    def app_subdir(self) -> Path:
        parts = filter(None, (self.url, self.org, self.app))
        return Path('.'.join(parts))
