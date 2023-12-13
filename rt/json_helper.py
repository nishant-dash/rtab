import json
from rich.console import Console

# project deps
from base_helper import BaseToRichTable

# Initialize console object for print
console = Console()


class JsonToRichTable(BaseToRichTable):
    def load(self, data) -> {}:
        loaded_data = None
        try:
            loaded_data = json.load(data)
        except json.JSONDecodeError as error:
            console.print(error)
        return loaded_data
