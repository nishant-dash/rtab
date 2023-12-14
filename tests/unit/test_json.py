"""Testing module for json capabilities of rt."""

import runpy
from unittest import mock

from rich.console import Console

from rt.json_helper import JsonToRichTable


@mock.patch("rt.cli.entrypoint")
def test_cli_init(cli):
    runpy.run_path("rt/__main__.py", run_name="__main__")
    cli.aassert_called_once_with()
