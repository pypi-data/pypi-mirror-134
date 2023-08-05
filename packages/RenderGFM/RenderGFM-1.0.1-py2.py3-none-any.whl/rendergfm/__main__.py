# This file is part of RenderGFM
#   <https://brettcsmith.org/RenderGFM>
# Copyright © 2022 Brett Smith <brettcsmith@brettcsmith.org>
# You may use, share, and modify this software under the terms of the
# Apache License 2.0
#   <https://opensource.org/licenses/Apache-2.0>

import argparse
import enum
import logging
import os
import signal
import sys
import types

from collections.abc import (
    Sequence,
)
from pathlib import Path
from requests.exceptions import HTTPError, RequestException
from typing import (
    cast,
    NoReturn,
    Optional,
    TextIO,
    Type,
)

from . import GitHubV3MarkdownRenderer, CLIEnum, RenderMode, VERSION, logger

STDSTREAM_PATH = Path('-')

_run_main = __name__ == '__main__'

class ExceptHook:
    def __init__(self, logger: logging.Logger=logger, level: int=logging.CRITICAL) -> None:
        self.logger = logger
        self.loglevel = level

    def __call__(self,
                 exc_type: Type[BaseException],
                 exc_value: BaseException,
                 exc_tb: Optional[types.TracebackType]=None,
    ) -> NoReturn:
        if isinstance(exc_value, HTTPError):
            msg = "HTTP error: {req.method} {req.url}: {res.reason} ({res.status_code})".format(
                req=exc_value.request,
                res=exc_value.response,
            )
            status_code = exc_value.response.status_code or -1
            exitcode = os.EX_TEMPFAIL if 500 <= status_code < 600 else os.EX_UNAVAILABLE
        elif isinstance(exc_value, RequestException):
            msg = "HTTP {name} on {req.method} {req.url}".format(
                name=exc_type.__name__,
                req=exc_value.request,
            )
            exitcode = os.EX_TEMPFAIL
        elif isinstance(exc_value, OSError):
            msg = "I/O error: {e.filename}: {e.strerror}".format(e=exc_value)
            exitcode = os.EX_IOERR
        elif isinstance(exc_value, KeyboardInterrupt):
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            os.kill(0, signal.SIGINT)
            signal.pause()
        else:
            msg = ": ".join([f"internal {exc_type.__name__}", *exc_value.args])
            exitcode = os.EX_SOFTWARE
        self.logger.log(self.loglevel, msg, exc_info=self.logger.isEnabledFor(logging.DEBUG))
        os._exit(exitcode)


class LogLevel(CLIEnum):
    CRIT = logging.CRITICAL
    CRITICAL = CRIT
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    FATAL = CRITICAL
    INFO = logging.INFO
    INFORMATION = INFO
    NOTE = INFO
    NOTICE = INFO
    WARN = logging.WARNING
    WARNING = WARN


def parse_arguments(arglist: Optional[Sequence[str]]=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='rendergfm',
        usage="%(prog)s [-O HTML_FILE] [MARKDOWN_FILE]",
        description="Render Markdown to HTML using the GitHub API",
    )
    parser.add_argument(
        '--output-file', '--html-file', '-O',
        metavar='PATH',
        type=Path,
        default=STDSTREAM_PATH,
        help="Path to write rendered HTML. Default stdout.",
    )
    parser.add_argument(
        '--mode', '-m',
        type=RenderMode.from_str,
        default=RenderMode.GFM,
        help="""Rendering mode. Choices are gfm (for GitHub-Flavored Markdown)
or plain (for regular Markdown). Default gfm.
""")
    parser.add_argument(
        '--context', '-c',
        help="""Rendering context. Pass a repository path (like
`brettcs/RenderGFM`) to automatically generate GitHub links to issues, pull
requests, etc.
""")
    parser.add_argument(
        '--log-level', '--loglevel',
        metavar='LEVEL',
        type=LogLevel.from_str,
        help="Show log messages at this level and above."
        " Choices are debug, info, warning, error, and critical."
        " Default info.",
    )
    parser.add_argument(
        'markdown_file',
        metavar='PATH',
        type=Path,
        default=STDSTREAM_PATH,
        help="Path to read Markdown source. Default stdin.",
    )
    return parser.parse_args()

def stdopen(path: Path, stream: TextIO, mode: str='r') -> TextIO:
    if path == STDSTREAM_PATH:
        return stream
    else:
        return cast(TextIO, path.open(mode))

def main(arglist: Optional[Sequence[str]]=None) -> int:
    if _run_main:
        sys.excepthook = ExceptHook()
        logging.basicConfig(
            format='%(name)s: %(levelname)s: %(message)s',
            level=logging.INFO,
        )
    args = parse_arguments(arglist)
    if args.log_level is not None:
        main_logger = logging.getLogger() if _run_main else logger
        main_logger.setLevel(args.log_level.value)

    with stdopen(args.markdown_file, sys.stdin) as in_file:
        markdown_source = in_file.read()

    renderer = GitHubV3MarkdownRenderer()
    render_result = renderer.render(markdown_source, args.mode, args.context)
    logger.debug(
        "%s render returned %s %s",
        render_result.url,
        render_result.status_code,
        render_result.reason,
    )
    render_result.raise_for_status()

    with stdopen(args.output_file, sys.stdout, 'w') as out_file:
        out_file.write(render_result.text)

    return os.EX_OK

if __name__ == '__main__':
    exit(main())
