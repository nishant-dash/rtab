"""Testing module for main entrypoint into rtab cli."""

import runpy
from unittest import mock


@mock.patch("rtab.cli.entrypoint")
def test_cli_init(cli):
    runpy.run_path("rtab/__main__.py", run_name="__main__")
    cli.assert_called_once_with()
