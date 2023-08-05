from typing import List, Union
from urllib.parse import parse_qs, urlencode

qs_value = Union[str, List[str]]


class Query:
    __slots__ = ["_data"]

    def __init__(self, query_string: str = ""):
        self._data = parse_qs(query_string, keep_blank_values=True)

    def __str__(self) -> str:
        return urlencode(self._data, doseq=True)

    def __repr__(self):
        return f"Query('{self}')"

    def __bool__(self) -> bool:
        return bool(self._data)

    def add(self, **kwargs: qs_value) -> None:
        for key, value in kwargs.items():
            self._data.setdefault(key, [])
            if isinstance(value, list):
                self._data[key].extend(value)
            else:
                self._data[key].append(value)

    def set(self, **kwargs: qs_value) -> None:  # noqa: A003
        for key, value in kwargs.items():
            self._data.setdefault(key, [])
            if isinstance(value, list):
                self._data[key] = value
            else:
                self._data[key] = [value]

    def replace(self, key: str, old_value: str, new_value: str) -> None:
        for i, value in enumerate(self._data.get(key, [])):
            if value == old_value:
                self._data[key][i] = new_value

    def remove(self, key: str) -> None:
        del self._data[key]
