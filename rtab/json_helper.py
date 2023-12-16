"""Load json data from stdin or file handler and print a rich table."""

import json

from rich.console import Console

# project deps
from rtab.base_helper import BaseToRichTable

# Initialize console object for print
console = Console()


class JsonToRichTable(BaseToRichTable):
    """This class inherits BaseToRichTable and loads json data to print a rich table out of."""

    def load(self, data) -> dict:  # pylint: disable=missing-type-doc
        """Load json data from stdin or file handler.

        :param data: Can be either a string or file handler, used to load data from
        """
        loaded_data = None
        try:
            loaded_data = json.load(data)
        except json.JSONDecodeError as error:
            console.print(error)
        return loaded_data
