# This file is part of RenderGFM
#   <https://brettcsmith.org/RenderGFM>
# Copyright © 2022 Brett Smith <brettcsmith@brettcsmith.org>
# You may use, share, and modify this software under the terms of the
# Apache License 2.0
#   <https://opensource.org/licenses/Apache-2.0>

import enum
import logging

import requests

from urllib import parse as urlparse

from typing import (
    NamedTuple,
    Optional,
    Type,
    TypeVar,
)

ET = TypeVar('ET', bound=enum.Enum)

logger = logging.getLogger('RenderGFM')

class _Version(NamedTuple):
    major: int
    minor: int
    micro: int = 0

    def __str__(self) -> str:
        return '.'.join(str(n) for n in self)
VERSION = _Version(1, 0, 1)


class CLIEnum(enum.Enum):
    @classmethod
    def from_str(cls: Type[ET], s: str) -> ET:
        try:
            return cls[s.upper()]
        except KeyError:
            raise ValueError(f"unknown {cls.__name__} {s!r}") from None


class RenderMode(CLIEnum):
    GITHUB_FLAVORED_MARKDOWN = 'gfm'
    GITHUB = GITHUB_FLAVORED_MARKDOWN
    GFM = GITHUB_FLAVORED_MARKDOWN
    GH = GITHUB_FLAVORED_MARKDOWN
    MARKDOWN = 'markdown'
    PLAIN = MARKDOWN


class GitHubV3MarkdownRenderer:
    API_ROOT = 'https://api.github.com/'
    API_PATH = 'markdown'

    def __init__(self, url: Optional[str]=None) -> None:
        if url is None:
            url = urlparse.urljoin(self.API_ROOT, self.API_PATH)
        self.url = url
        self.headers = requests.utils.default_headers()
        self.headers['Accept'] = 'application/vnd.github.v3+json'
        self.headers['User-Agent'] = f"RenderGFM/{VERSION} ({self.headers['User-Agent']})"

    def render(self,
               markdown: str,
               mode: RenderMode=RenderMode.GFM,
               context: Optional[str]=None,
               ) -> requests.Response:
        req_body = {
            'mode': mode.value,
            'text': markdown,
        }
        if context is not None:
            req_body['context'] = context
        return requests.post(self.url, headers=self.headers, json=req_body)
