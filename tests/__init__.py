import random
import string
from pathlib import Path


def random_str(length: int, /) -> str:
    return ''.join(random.choices(string.ascii_letters, k=length))

# Descriptive package and use random values to avoid bias
PKG: Path = Path("/outside/work/repository/package")
APP: str = f"app-{random_str(16)}"
ORG: str = f"org-{random_str(16)}"
URL: str = f"url-{random_str(3)}"
