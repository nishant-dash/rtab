import yaml
from rich.console import Console

# project deps
from base_helper import BaseToRichTable

# Initialize console object for print
console = Console()


class YamlToRichTable(BaseToRichTable):
    def load(self, data) -> {}:
        loaded_data = None
        try:
            loaded_data = yaml.safe_load(data)
        except yaml.YAMLError as error:
            console.print(error)
        return loaded_data
