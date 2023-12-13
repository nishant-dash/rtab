"""This module definies a Base class to dictate loading and printing rich table data."""

from abc import abstractmethod

from rich import box
from rich.console import Console
from rich.table import Table

# Initialize console object for print
console = Console()


class BaseToRichTable:
    """Base class to defines a layout of loading and printing rich table data."""

    def __init__(self, **kwargs) -> None:
        """Initialize input dict as class attributes."""
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abstractmethod
    def load(self, data) -> dict:  # pylint: disable=missing-type-doc
        """Load data in from a file or variable.

        :param data: Can be either a string or file handler, used to load data from
        """
        return

    def create_table(self) -> Table:
        """Create a rich table object."""
        # pylint: disable=maybe-no-member
        return Table(box=box.ROUNDED, highlight=not self.suppress)

    def pre_run(self, stdin_data, skip_load: bool = False):  # pylint: disable=missing-type-doc
        """Do some basic checks and return loaded data.

        :param stdin_data: Can be either a string or file handler, used to load data from
        :param skip_load: used to skip the call to load if data is pre-loaded into stdin_data
        """
        data = None
        if skip_load:
            data = stdin_data
        else:
            data = self.load(stdin_data)
        if not data:
            console.print(f"Can not load stdin into {type(self).__name__}")
        return data, type(data)

    def run(self, stdin_data, skip_load: bool = False) -> None:  # pylint: disable=missing-type-doc
        """Load stdin as json and transform into rich table.

        :param stdin_data: Can be either a string or file handler, used to load data from
        :param skip_load: used to skip the call to load if data is pre-loaded into stdin_data
        """
        data, data_type = self.pre_run(stdin_data, skip_load)
        if not data:
            return

        # Initialize table object
        table = self.create_table()

        if data_type == dict:
            # Show Logic
            table.add_column("Key")
            table.add_column("Value")
            for k, v in data.items():
                table.add_row(k, str(v))
        elif data_type == list:
            # List Logic
            columns = list(data[0].keys())
            for c in columns:
                table.add_column(c)
            for r in data:
                temp_row = [str(v) for v in r.values()]
                table.add_row(*temp_row)
        else:
            console.print(f"Unsupported type {data_type}")
            return

        console.print(table)
