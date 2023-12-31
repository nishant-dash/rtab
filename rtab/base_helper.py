"""This module definies a Base class to dictate loading and printing rich table data."""

from abc import ABC, abstractmethod
from typing import Dict, List

from rich import box
from rich.console import Console
from rich.table import Table

from rtab.context_highlighter import Dispatcher

# Initialize console object for print
console = Console()


class BaseToRichTable(ABC):
    """Base class to defines a layout of loading and printing rich table data."""

    def __init__(self, **kwargs) -> None:
        """Initialize input dict as class attributes."""
        self.table = None
        self.quiet = False
        self.separator = ""
        self.wrap = False
        self.lines = False
        self.rule = ""
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abstractmethod
    def load(self, data) -> dict:  # pylint: disable=missing-type-doc
        """Load data in from a file or variable.

        :param data: Can be either a string or file handler, used to load data from
        """
        return

    def create_table(self) -> None:
        """Create a rich table object."""
        # pylint: disable=maybe-no-member
        self.table = Table(box=box.ROUNDED, highlight=not self.quiet, show_lines=self.lines)

    def add_column(self, column: str = "") -> None:
        """Add a column to a rich table object.

        :param column: A string to add to the table as a column header
        """
        # pylint: disable=maybe-no-member
        (self.table).add_column(column, overflow="fold" if self.wrap else "ellipsis")

    def add_row(self, row: list = None) -> None:
        """Add a row to a rich table object.

        :param row: A list to add to the table as a row
        """
        # highlighter = ContextHighlight(self.rules)
        # formatted_row = highlighter.apply_highlights(row)
        (self.table).add_row(*row)

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
        return data

    def console_print(self) -> None:
        """Get custom rich console object and print.

        If rule is not specified as a cli flag, then the default rich console object is used.
        """
        dc = Dispatcher()
        custom_console = dc.get_console(self.rule)
        custom_console.print(self.table)

    def run(self, stdin_data, skip_load: bool = False) -> int:  # pylint: disable=missing-type-doc
        """Load stdin as json and transform into rich table.

        :param stdin_data: Can be either a string or file handler, used to load data from
        :param skip_load: used to skip the call to load if data is pre-loaded into stdin_data
        """
        data = self.pre_run(stdin_data, skip_load)
        if not data:
            return 1

        # Initialize table object
        self.create_table()

        if isinstance(data, Dict):
            # Show Logic
            self.add_column("Key")
            self.add_column("Value")
            for k, v in data.items():
                self.add_row([k, str(v)])
        elif isinstance(data, List):
            # List Logic
            columns = list(data[0].keys())
            for c in columns:
                self.add_column(c)
            for r in data:
                self.add_row([str(v) for v in r.values()])
        else:
            console.print(f"Unsupported type {type(data)}")
            return 1

        # Print the table
        self.console_print()

        return 0
