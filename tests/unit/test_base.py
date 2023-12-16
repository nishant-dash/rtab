"""Testing module for base class of rtab."""

from unittest.mock import patch

import pytest
from rich.table import Table

from rtab.base_helper import BaseToRichTable


def test_create_table():
    obj = BaseToRichTable(**{"suppress": False})
    data = obj.create_table()
    assert type(data) is Table


def test_pre_run_success():
    obj = BaseToRichTable(**{"suppress": False})
    test_data = [{"test": "data"}]
    data, td = obj.pre_run(test_data, skip_load=True)
    assert td == list
    assert data == test_data


def test_pre_run_failure():
    obj = BaseToRichTable(**{"suppress": False})
    test_data = None
    data, _ = obj.pre_run(test_data, skip_load=True)
    assert data == test_data


@pytest.mark.parametrize(
    "mock_data",
    [
        [{"test": "data"}],
        {"test": "data"},
    ],
)
def test_run_success(mock_data):
    obj = BaseToRichTable(**{"suppress": False})
    assert obj.run(mock_data, skip_load=True) == 0


@pytest.mark.parametrize(
    "mock_ret_value, mock_ret_type",
    [
        (("a", "b"), tuple),
        (None, None),
    ],
)
@patch("rtab.base_helper.BaseToRichTable.pre_run")
def test_run_failure(mock_pre_run, mock_ret_value, mock_ret_type):
    mock_pre_run.return_value = mock_ret_value, mock_ret_type
    obj = BaseToRichTable(**{"suppress": False})
    test_data = [{"test": "data"}]
    assert obj.run(test_data, skip_load=True) == 1
