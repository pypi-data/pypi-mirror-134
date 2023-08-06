import logging
from typing import Any, Optional

import dice_lib.parameters as dice_params
import rich
import typer

from . import __version__, admin, benchmark, docs, info, job
from .logger import admin_logger, console_handler, user_logger


def user_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug output"),
) -> Any:
    # verbose is debug
    verbose = debug or verbose
    debug = verbose

    if debug:
        user_logger.setLevel(logging.DEBUG)
        # workaround for rich
        console_handler.setLevel(logging.DEBUG)


def admin_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Debug output"),
) -> Any:
    # verbose is debug
    verbose = debug or verbose
    debug = verbose

    if debug:
        admin_logger.setLevel(logging.DEBUG)
        # workaround for rich
        console_handler.setLevel(logging.DEBUG)


app = typer.Typer()
app.add_typer(admin.app, name="admin", callback=admin_callback)
app.add_typer(benchmark.app, name="benchmark", callback=user_callback)
app.add_typer(docs.app, name="docs", callback=user_callback)
app.add_typer(info.app, name="info", callback=user_callback)
app.add_typer(job.app, name="job", callback=user_callback)


@app.command()
def version() -> None:
    """
    Show version
    """
    rich.print(f"[blue]DICE CLI Version[/]: [magenta]{__version__}[/]")


@app.command()
def glossary(
    word: Optional[str] = typer.Argument(None, help="Word to search for"),
    print_all: bool = typer.Option(
        False, "--all", "-a", help="Print all glossary entries"
    ),
) -> None:
    """
    Show the meaning of a given word (in DICE context)
    """
    if print_all:
        rich.print("[blue]All items[/]:")
        for w, meaning in dice_params.GLOSSARY.items():
            rich.print(f"[blue]{w}[/]: [magenta]{meaning}[/]")
        return

    if word not in dice_params.GLOSSARY:
        rich.print(f"[red]Word '{word}' not found[/]")
        typer.echo("To list all glossary items use 'dice glossary -a'")
        return

    rich.print(f"[blue]{word}[/]: [magenta]{dice_params.GLOSSARY[word]}[/]")


def main() -> Any:
    return app()
