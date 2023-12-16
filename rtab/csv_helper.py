"""Load csv data from stdin or file handler and print a rich table."""

import csv

from rich.console import Console

# project deps
from rtab.base_helper import BaseToRichTable

# Initialize console object for print
console = Console()


class CsvToRichTable(BaseToRichTable):
    """This class inherits BaseToRichTable and loads csv data to print a rich table out of."""

    def load(self, data) -> list:  # type: ignore[override] # pylint: disable=missing-type-doc
        """Load data as csv, i.e, a list of list of strings.

        :param data: Can be either a string or file handler, used to load data from
        """
        # @TODO try playing with Dictreader?
        loaded_data = []
        try:
            # pylint: disable=maybe-no-member
            for line in csv.reader(data.readlines()):
                formatted_line = []
                for elem in line:
                    formatted_elem = " ".join(elem.split())
                    elem_to_add = [formatted_elem]
                    if self.separator:
                        elem_to_add = formatted_elem.split(self.separator)
                    formatted_line.extend(elem_to_add)
                loaded_data.append(formatted_line)
        except IOError as error:
            console.print(error)
            return None
        return loaded_data

    def run(self, stdin_data, skip_load: bool = False) -> int:  # pylint: disable=missing-type-doc
        """Load stdin as csv data and transform into rich table.

        :param stdin_data: Can be either a string or file handler, used to load data from
        :param skip_load: used to skip the call to load if data is pre-loaded into stdin_data
        """
        data, data_type = self.pre_run(stdin_data, skip_load)
        if not data:
            return 1

        # Initialize table object
        table = self.create_table()

        if data_type == list:
            for column in list(data[0]):
                table.add_column(column)
            for row in data[1:]:
                table.add_row(*row)
        else:
            console.print(f"Csv reader can't handle {data_type}")
            return 1

        console.print(table)
        return 0
