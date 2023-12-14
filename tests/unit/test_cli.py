"""Testing module for json capabilities of rt."""

from unittest.mock import patch

from rt import cli


@patch("rt.json_helper.JsonToRichTable.run")
def test_json_cli(fn):
    cli.main(is_json=True)
    fn.assert_called_once()


@patch("rt.yaml_helper.YamlToRichTable.run")
def test_yaml_cli(fn):
    cli.main(is_yaml=True)
    fn.assert_called_once()


@patch("rt.csv_helper.CsvToRichTable.run")
def test_csv_cli(fn):
    cli.main(is_csv=True)
    fn.assert_called_once()
