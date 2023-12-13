# rt.
from json_helper import JsonToRichTable
from yaml_helper import YamlToRichTable
from csv_helper import CsvToRichTable

# cli
import typer
from typing_extensions import Annotated

# console and formatting
from rich.console import Console

# misc.
import sys


cli = typer.Typer(
    name="rt",
    rich_markup_mode="rich",
    add_completion=False,
    help="""
    A simple formatting cli that converts json, yaml and csv into tables using the rich library
    """,
)

console = Console()


@cli.command()
def main(
    is_json: Annotated[
        bool,
        typer.Option(
            "-j",
            "--json",
            help="Format json into rich tables",
        ),
    ] = False,
    is_yaml: Annotated[
        bool,
        typer.Option(
            "-y",
            "--yaml",
            help="Format yaml into rich tables",
        ),
    ] = False,
    is_csv: Annotated[
        bool,
        typer.Option(
            "-c",
            "--csv",
            help="Format csv into rich tables",
        ),
    ] = False,
    invert: Annotated[
        bool,
        typer.Option(
            "-i",
            "--invert",
            help="Invert the table matrix output",
        ),
    ] = False,
):
    """
    :sparkles: A simple formatting cli that converts json, yaml and csv into tables using the rich library
    """
    stdin_data = sys.stdin
    extra_options = {
        "invert": invert,
    }
    if is_json:
        obj = JsonToRichTable(**extra_options)
    elif is_yaml:
        obj = YamlToRichTable(**extra_options)
    elif is_csv:
        obj = CsvToRichTable(**extra_options)
    else:
        console.print("[red]Unsupported![/red]")
        return
    obj.run(stdin_data)


def entrypoint() -> None:
    cli()


if __name__ == "__main__":
    entrypoint()
