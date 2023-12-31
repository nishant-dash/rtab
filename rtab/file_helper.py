"""Load data from a file and print a rich table."""

from pathlib import Path

from rich.console import Console

from rtab.csv_helper import CsvToRichTable
from rtab.json_helper import JsonToRichTable
from rtab.yaml_helper import YamlToRichTable

# Initialize console object for print
console = Console()


class FileToRichTable:
    """This class uses other helper classes to load data correctly to print a rich table."""

    def __init__(self, **kwargs):
        """Initialize inputs dict class variables."""
        self.options = kwargs
        self.obj = None

    def load(self, filename: str) -> dict:  # pylint: disable=missing-type-doc
        """Load data from filename using extrapolated object based on file extension.

        :param filename: Name of the file to load data from
        """
        data = None
        try:
            with open(filename, "r", encoding="utf-8") as f:
                if self.obj:
                    data = self.obj.load(f)
        except IOError as error:
            console.print(error)
        return data

    def run(self, filename: str) -> int:
        """Print rich table using extrapolated object based on file extension.

        :param filename: Name of the file to load data from
        """
        file_path = Path(filename)
        match file_path.suffix:
            case ".json":
                self.obj = JsonToRichTable(**self.options)
            case ".yaml":
                self.obj = YamlToRichTable(**self.options)
            case ".csv":
                self.obj = CsvToRichTable(**self.options)
            case _:
                console.print(f"Unsupported file extension '{file_path}'")
                return 1

        loaded_data = self.load(filename)
        if loaded_data:
            self.obj.run(loaded_data, skip_load=True)
        return 0
