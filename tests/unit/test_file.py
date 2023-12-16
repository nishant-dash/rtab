"""Testing module for file input capabilities of rtab."""

from unittest.mock import patch

import pytest

from rtab import cli
from rtab.file_helper import FileToRichTable


@pytest.mark.parametrize(
    "mode",
    [("Json"), ("Yaml"), ("Csv")],
)
def test_file_types(mode):
    with patch(f"rtab.{mode.lower()}_helper.{mode}ToRichTable.load") as mocker:
        cli.main(file=f"tests/resources/test.{mode.lower()}")
        mocker.assert_called_once()


@pytest.mark.parametrize(
    "mode, mock_ret_value",
    [
        ("json", 0),
        ("yaml", 0),
        ("csv", 0),
        ("conf", 1),
    ],
)
def test_file_types_with_failure(mode, mock_ret_value):
    obj = FileToRichTable(**{"quiet": False})
    ret = obj.run(f"tests/resources/test.{mode}")
    assert ret == mock_ret_value
