import sys
import json
from rich.console import Console
from rich.table import Table
from rich import box

# Initialize console object for print
console = Console()

# load stdin
try:
    data = json.load(sys.stdin)
except json.JSONDecodeError as error:
    console.print(error)
    exit(1)

# Initialize table object and misc.
table = Table(box=box.ROUNDED, highlight=True)
td = type(data)
columns = None

# List Logic
if td == list:
    columns = [k for k in data[0].keys()]
    for c in columns:
        table.add_column(c)
    for r in data:
        temp_row = [str(v) for v in r.values()]
        table.add_row(*temp_row)
elif td == dict:
    # Show Logic
    table.add_column("Key")
    table.add_column("Value")
    for k, v in data.items():
        table.add_row(k, str(v))
else:
    console.print(f"Unsupported type {td}")
    exit(1)

console.print(table)
