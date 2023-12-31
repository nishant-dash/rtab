"""Testing module for base class of rtab."""

from unittest.mock import patch

import pytest
from rich.table import Table

from rtab.base_helper import BaseToRichTable


@patch.multiple(BaseToRichTable, __abstractmethods__=set())
def test_create_table():
    obj = BaseToRichTable()
    obj.create_table()
    assert type(obj.table) is Table


@patch.multiple(BaseToRichTable, __abstractmethods__=set())
def test_pre_run_success():
    obj = BaseToRichTable()
    test_data = [{"test": "data"}]
    data, td = obj.pre_run(test_data, skip_load=True)
    assert td == list
    assert data == test_data


@patch.multiple(BaseToRichTable, __abstractmethods__=set())
def test_pre_run_failure():
    obj = BaseToRichTable()
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
@patch.multiple(BaseToRichTable, __abstractmethods__=set())
def test_run_success(mock_data):
    obj = BaseToRichTable()
    assert obj.run(mock_data, skip_load=True) == 0


@pytest.mark.parametrize(
    "mock_ret_value, mock_ret_type",
    [
        (("a", "b"), tuple),
        (None, None),
    ],
)
@patch.multiple(BaseToRichTable, __abstractmethods__=set())
@patch("rtab.base_helper.BaseToRichTable.pre_run")
def test_run_failure(mock_pre_run, mock_ret_value, mock_ret_type):
    mock_pre_run.return_value = mock_ret_value, mock_ret_type
    obj = BaseToRichTable()
    test_data = [{"test": "data"}]
    assert obj.run(test_data, skip_load=True) == 1
