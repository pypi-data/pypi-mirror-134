from pathlib import Path
from typing import List, Optional

import typer
from dice_lib.date import current_formatted_date

from dice_cli._io import write_list_data_to_csv
from dice_cli.logger import admin_logger

from ._storage import generate_storage_report

app = typer.Typer(help="Commands for report creation")


@app.command()
def storage(
    paths: List[Path] = typer.Argument(...),
    output_directory: Optional[Path] = typer.Option(
        None,
        "-o",
        "--output",
        help="Output directory",
    ),
    resolve_usernames: bool = typer.Option(False, "--resolve-usernames"),
) -> None:
    """
    Generate a report of the storage usage of the given paths.

    :param paths: The paths to generate the report for.
    :param output_directory: The directory to write the report to.
    :param resolve_usernames: Whether to resolve usernames to their real names.
    """
    if not output_directory:
        today = current_formatted_date()
        output_directory = Path(f"/tmp/{today}_dice_admin_storage_report.csv")

    headers, report = generate_storage_report(paths, resolve_usernames)
    write_list_data_to_csv(report, headers, output_directory)

    admin_logger.info(f"Report saved to {output_directory}")
