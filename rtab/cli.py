"""Main CLI module for rtab.

This module defines the cli options and arguments for rtab.
"""

import sys
from typing import Optional

import typer
from rich.console import Console
from typing_extensions import Annotated

from rtab.csv_helper import CsvToRichTable
from rtab.file_helper import FileToRichTable
from rtab.json_helper import JsonToRichTable
from rtab.yaml_helper import YamlToRichTable

OPENSTACK_RED = "bold #F20B4B"
OPENSTACK_BLUE = "bold #19ADE5"
JUJU = "bold #E95420"
KUBERNETES = "bold #3970E4"

cli = typer.Typer(
    name="rtab",
    rich_markup_mode="rich",
    add_completion=False,
    help="""
    A simple formatting cli that converts json, yaml and csv into tables using the rich library
    """,
)

console = Console()


@cli.command(
    epilog="""
    Visit :link:
[green link=https://github.com/nishant-dash/rtab]github.com/nishant-dash/rtab[/green link]
for more info!
    """,
    help="""
    :sparkles: A simple formatting cli that converts [bold]json[/bold], [bold]yaml[/bold] or
[bold]csv[/bold] into tables using the :link: [link=https://github.com/Textualize/rich]rich[/link]
library.
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
    quiet: Annotated[
        bool,
        typer.Option(
            "-q",
            "--quiet",
            help="Suppress highlighting",
            rich_help_panel="Modifiers",
        ),
    ] = False,
    separator: Annotated[
        str,
        typer.Option(
            "-s",
            "--separator",
            help="Specify an input separator, only applies with csv input '[bold]-c[/bold]'",
            rich_help_panel="Modifiers",
            show_default=False,
        ),
    ] = "",
    wrap: Annotated[
        bool,
        typer.Option(
            "-w",
            "--wrap",
            help="Allow wrapping of text in rows, helpful if row is long",
            rich_help_panel="Modifiers",
        ),
    ] = False,
    lines: Annotated[
        bool,
        typer.Option(
            "-l",
            "--lines",
            help="Show lines between rows",
            rich_help_panel="Modifiers",
        ),
    ] = False,
    rule: Annotated[
        str,
        typer.Option(
            "-r",
            "--rule",
            help=f"""
            Use special highlighting rules for tools such as
            [{OPENSTACK_RED}]open[/{OPENSTACK_RED}][{OPENSTACK_BLUE}]stack[/{OPENSTACK_BLUE}],\n
            [{JUJU}]juju[/{JUJU}], and [{KUBERNETES}]kubernetes[/{KUBERNETES}]
            """,
            rich_help_panel="Context Highlighting",
        ),
    ] = "",
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
    :param quiet: Suppress highlighting
    :param separator: Specify a separator, only applies with table input '-t'
    :param rule: Add special highlighting rules such as openstack, juju, kubernetes, etc...
    :param wrap: Allow wrapping of text in rows, helpful if row is long
    :param lines: Show lines between rows
    :param file: Specify a file (file extension matters!)
    :raises Exit: 1 if no defining input is provided
    """
    stdin_data = sys.stdin
    extra_options = {
        "quiet": quiet,
        "separator": separator,
        "rule": rule,
        "wrap": wrap,
        "lines": lines,
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
        raise typer.Exit(code=1)
    return obj.run(stdin_data)  # type: ignore[arg-type]


def entrypoint() -> None:
    """Entrypoint into cli of rtab."""
    cli()
