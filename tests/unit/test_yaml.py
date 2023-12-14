"""Testing module for yaml capabilities of rt."""

from rt.yaml_helper import YamlToRichTable


def test_read_yaml():
    test_data = [{"test": "test1", "test2": [{"test3": "test4"}]}]
    with open("tests/resources/test_small.yaml", "r") as f:
        obj = YamlToRichTable()
        data = obj.load(f)
        assert data == test_data
