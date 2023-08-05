# RenderGFM

RenderGFM is a command-line tool that renders Markdown to HTML exactly how GitHub does it.

This tool calls the GitHub API to convert Markdown to HTML. Use this to check that your document will look the way you want on GitHub without cluttering your Git history.

## Installation

[Install Python 3][] and run:

      python3 -m pip install --user RenderGFM

[Install Python 3]: https://wiki.python.org/moin/BeginnersGuide/Download

## Important Security Note

RenderGFM uploads your Markdown to GitHub servers. You should only use this tool on documents that you intend to publish on GitHub, and nothing private.

## Usage

Typical usage looks like:

      rendergfm -O README.html README.md

RenderGFM will write to standard output, and read from standard input, if you don't specify any file arguments. So you can equivalently run it like:

      rendergfm <README.md >README.html

Pass the `--context`/`-c` option to specify the repository you're working from, and automatically generate GitHub links to issues, pull requests, etc.

      rendergfm -c brettcs/RenderGFM README.md

There are additional options to control the rendering mode and enable debug logs. Run `rendergfm --help` for details.

## Limitations

The HTML output isn't stylized at all. It's still enough to check for correctness, but the tool could add some CSS to make it easier to read.

## RenderGFM is free software

RenderGFM is copyright © 2022 by [Brett Smith](mailto:brettcsmith@brettcsmith.org). You can use, share, and modify the program under the terms of the included [Apache License 2.0](LICENSE.txt).
