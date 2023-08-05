from typing import Union
from urllib.parse import urljoin, urlparse

from pathurl.constants import Port
from pathurl.path import Path
from pathurl.query import Query


class URL:
    __slots__ = [
        "scheme",
        "username",
        "password",
        "hostname",
        "port",
        "path",
        "query",
        "fragment",
    ]

    def __init__(
        self,
        *,
        scheme: str = "",
        username: str = None,
        password: str = None,
        hostname: str = None,
        port: int = None,
        path: str = "",
        query: str = "",
        fragment: str = "",
    ):
        self.scheme = scheme
        self.username = username
        self.hostname = hostname
        self.password = password
        self.port = port or self._infer_port(self.scheme)
        self.path = Path(path)
        self.query = Query(query)
        self.fragment = fragment

    def __str__(self) -> str:
        parts = []
        if self.scheme:
            parts.append(f"{self.scheme}:")
        parts.append("//")
        if self.username or self.password:
            if self.username:
                parts.append(self.username)
            if self.password:
                parts.append(f":{self.password}")
            parts.append("@")
        parts.append(self.hostname)
        if self.port and self.port != self._infer_port(self.scheme):
            parts.append(f":{self.port}")
        parts.append(str(self.path))
        if self.query:
            parts.append(f"?{self.query}")
        if self.fragment:
            parts.append(f"#{self.fragment}")
        return "".join(parts)

    def __repr__(self):
        return f"URL('{self}')"

    @staticmethod
    def _infer_port(scheme: str) -> int:
        try:
            port = Port[scheme]
        except KeyError:
            return None

        return port.value

    def join(self, path: Union[str, Path]) -> "URL":
        return self.__class__.from_string(urljoin(str(self), str(path)))

    @classmethod
    def parse(cls, url: str) -> "URL":
        parsed_url = urlparse(url)
        return cls(
            scheme=parsed_url.scheme,
            username=parsed_url.username,
            password=parsed_url.password,
            hostname=parsed_url.hostname,
            port=parsed_url.port,
            path=parsed_url.path,
            query=parsed_url.query,
            fragment=parsed_url.fragment,
        )

    @classmethod
    def from_string(cls, url: str) -> "URL":
        return cls.parse(url)
