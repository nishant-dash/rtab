"""Load yaml data from stdin or file handler and print a rich table."""

import yaml
from rich.console import Console

# project deps
from rt.base_helper import BaseToRichTable

# Initialize console object for print
console = Console()


class YamlToRichTable(BaseToRichTable):
    """This class inherits BaseToRichTable and loads yaml data to print a rich table out of."""

    def load(self, data) -> dict:  # pylint: disable=missing-type-doc
        """Load yaml data from stdin or file handler.

        :param data: Can be either a string or file handler, used to load data from
        """
        loaded_data = None
        try:
            loaded_data = yaml.safe_load(data)
        except yaml.YAMLError as error:
            console.print(error)
        return loaded_data
