import csv
from rich.console import Console
from rich.table import Table
from rich import box

# project deps
from base_helper import BaseToRichTable

# Initialize console object for print
console = Console()


class CsvToRichTable(BaseToRichTable):
    def load(self, data) -> []:
        # @TODO try playing with Dictreader?
        loaded_data = []
        try:
            for line in csv.reader(data.readlines()):
                loaded_data.append(line)
        except Exception as error:
            console.print(error)
            return None
        return loaded_data

    def run(self, stdin_data) -> None:
        """
        Load stdin as json and transform into rich table
        """
        data = self.load(stdin_data)
        if not data:
            console.print(f"Can not load stdin into {type(self).__name__}")

        # Initialize table object and misc.
        table = self.create_table()
        td = type(data)
        columns = None

        if td == list:
            columns = [k for k in data[0]]
            for c in columns:
                table.add_column(c)
            for r in data[1:]:
                table.add_row(*r)
        else:
            console.print(f"Unsupported type {td}")
            return None

        console.print(table)
