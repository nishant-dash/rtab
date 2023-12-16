"""Testing module for json capabilities of rtab."""

from rtab.json_helper import JsonToRichTable


def test_read_json():
    test_data = [{"test": "data"}]
    with open("tests/resources/test_small.json", "r") as f:
        obj = JsonToRichTable()
        data = obj.load(f)
        assert data == test_data
