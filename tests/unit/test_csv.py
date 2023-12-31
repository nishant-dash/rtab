"""Testing module for csv capabilities of rtab."""

from unittest.mock import patch

import pytest

from rtab.csv_helper import CsvToRichTable


def test_load_csv():
    test_data = [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
    with open("tests/resources/test_small.csv", "r") as f:
        obj = CsvToRichTable()
        data = obj.load(f)
        assert data == test_data


def test_run_csv():
    with open("tests/resources/test_small.csv", "r") as f:
        obj = CsvToRichTable()
        assert 0 == obj.run(f)


@pytest.mark.parametrize(
    "mock_ret_value, mock_ret_type",
    [
        (("a", "b"), tuple),
        (None, None),
    ],
)
@patch("rtab.csv_helper.CsvToRichTable.pre_run")
def test_run_failure(mock_pre_run, mock_ret_value, mock_ret_type):
    mock_pre_run.return_value = mock_ret_value, mock_ret_type
    obj = CsvToRichTable()
    test_data = [["r1c1", "r1c2"], ["r2c1", "r2c2"]]
    assert obj.run(test_data, skip_load=True) == 1
