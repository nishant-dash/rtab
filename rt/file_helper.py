from pathlib import Path
from rich.console import Console

from json_helper import JsonToRichTable
from yaml_helper import YamlToRichTable
from csv_helper import CsvToRichTable

# Initialize console object for print
console = Console()


class FileToRichTable:
    def __init__(self, **kwargs):
        """Initialize inputs dict class variables."""
        self.options = kwargs
        self.obj = None

    def load(self, filename) -> {}:
        """Load data from filename using extrapolated object based on file extension."""
        data = None
        try:
            with open(filename, "r") as f:
                if self.obj:
                    data = self.obj.load(f)
        except IOError as error:
            console.print(error)
        return data

    def run(self, filename) -> None:
        """Print rich table using extrapolated object based on file extension."""
        file_path = Path(filename)
        match file_path.suffix:
            case ".json":
                self.obj = JsonToRichTable(**self.options)
            case ".yaml":
                self.obj = YamlToRichTable(**self.options)
            case ".csv":
                self.obj = CsvToRichTable(**self.options)
            case _:
                self.obj = None

        if self.obj:
            loaded_data = self.load(filename)
            if loaded_data:
                self.obj.run(loaded_data, skip_load=True)
