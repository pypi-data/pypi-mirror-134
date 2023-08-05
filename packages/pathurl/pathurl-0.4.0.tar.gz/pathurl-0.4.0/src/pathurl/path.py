from typing import List, Union
from urllib.parse import urljoin


class Path:
    __slots__ = ["_path"]

    def __init__(self, path: str = ""):
        self._path = path

    def __str__(self):
        return self._path

    def __repr__(self):
        return f"Path('{self}')"

    @property
    def is_absolute(self) -> bool:
        return not self._path or self._path.startswith("/")

    @property
    def segments(self) -> List[str]:
        split = self._path.split("/")
        if self.is_absolute:
            return split[1:]
        return split

    def join(self, path: Union[str, "Path"]) -> "Path":
        return self.__class__(urljoin(self._path, str(path)))
