"""Main CLI module for rt.

This module defines the cli options and arguments for rt.
"""

import sys
from typing import Optional

import typer
from rich.console import Console
from typing_extensions import Annotated

from rt.csv_helper import CsvToRichTable
from rt.file_helper import FileToRichTable
from rt.json_helper import JsonToRichTable
from rt.yaml_helper import YamlToRichTable

cli = typer.Typer(
    name="rt",
    rich_markup_mode="rich",
    add_completion=False,
    help="""
    A simple formatting cli that converts json, yaml and csv into tables using the rich library
    """,
)

console = Console()


@cli.command(
    epilog="""
    Visit :link: [green underline]https://github.com/nishant-dash/rt[/green underline]
for more info!
    """,
    help="""
    :sparkles: A simple formatting cli that converts [bold]json[/bold], [bold]yaml[/bold]
or [bold]csv[/bold] into tables using the rich library.
    """,
    # no_args_is_help=True,
)
def main(  # pylint: disable=too-many-arguments
    is_json: Annotated[
        bool,
        typer.Option(
            "-j",
            "--json",
            help="Format [bold]json[/bold] into rich tables",
        ),
    ] = False,
    is_yaml: Annotated[
        bool,
        typer.Option(
            "-y",
            "--yaml",
            help="Format [bold]yaml[/bold] into rich tables",
        ),
    ] = False,
    is_csv: Annotated[
        bool,
        typer.Option(
            "-c",
            "--csv",
            help="Format [bold]csv[/bold] into rich tables",
        ),
    ] = False,
    transpose: Annotated[
        bool,
        typer.Option(
            "-t",
            "--transpose",
            help="[bold]Transpose[/bold] the table output",
            rich_help_panel="Modifiers",
        ),
    ] = False,
    suppress: Annotated[
        bool,
        typer.Option(
            "-s",
            "--suppress",
            help="Suppress highlighting",
            rich_help_panel="Modifiers",
        ),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option(
            "-q",
            "--quiet",
            help="Suppress special keyword highlighting",
            rich_help_panel="Modifiers",
        ),
    ] = False,
    rules: Annotated[
        str,
        typer.Option(
            "-r",
            "--rules",
            help="""
            Add special highlighting ruels such as [bold blue]openstack[/bold blue],\n
            [bold red]juju[/bold red], etc...
            """,
            rich_help_panel="Context Highlighting",
        ),
    ] = None,
    file: Annotated[
        Optional[str],
        typer.Argument(
            help="Specify a file ([bold]file extension matters![/bold])",
        ),
    ] = None,
):
    """:sparkles: Convert json, yaml or csv into rich tables.

    :param is_json: Bool flag to format json into rich tables
    :param is_yaml: Bool flag to format yaml into rich tables
    :param is_csv: Bool flag to format csv into rich tables
    :param transpose: Bool flag to transpose the table output
    :param suppress: Suppress highlighting
    :param quiet: Suppress special keyword highlighting
    :param rules: Add special highlighting ruels such as openstack, juju, etc...
    :param file: Specify a file (file extension matters!)
    """
    stdin_data = sys.stdin
    extra_options = {
        "transpose": transpose,
        "suppress": suppress,
        "quiet": quiet,
        "rules": rules,
    }
    if file:
        obj = FileToRichTable(**extra_options)
        stdin_data = str(file)
    elif is_json:
        obj = JsonToRichTable(**extra_options)
    elif is_yaml:
        obj = YamlToRichTable(**extra_options)
    elif is_csv:
        obj = CsvToRichTable(**extra_options)
    else:
        console.print("[red]No file nor any one of json, yaml or csv chosen![/red]")
        return 1
    obj.run(stdin_data)  # type: ignore[arg-type]
    return 0


def entrypoint() -> None:
    """Entrypoint into cli of rt."""
    cli()


if __name__ == "__main__":
    entrypoint()
