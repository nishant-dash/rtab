# rt.

# cli
import typer

# console and formatting
from rich.console import Console


cli = typer.Typer(
    name="rt",
    rich_markup_mode="rich",
    add_completion=False,
    help="""
    A simple formatting cli that converts json, yaml and csv into tables using the rich library
    """,
)

console = Console()


def entrypoint() -> None:
    cli()


if __name__ == "__main__":
    entrypoint()
