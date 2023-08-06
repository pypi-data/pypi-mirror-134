import typer
from ..utils.serial_util import from_gpx_to_gps

from pathlib import Path
from typing import Optional

app = typer.Typer()


@app.command()
def to_gps(gpx_file: Optional[Path] = typer.Option(None, help="gpx file to upload")):
    if gpx_file is None:
        typer.echo("No file entered")
        raise typer.Abort()
    if gpx_file.is_file():
        typer.echo("\n" + "-" * 30)
        typer.echo(f"File {gpx_file} will be processed")
    elif not gpx_file.exists():
        typer.echo("The file doesn't exist")
        raise typer.Abort()

    typer.echo("\n" + "-" * 30)
    typer.echo("Connection to GP32 is good")
    typer.echo("Press 'Charge WP/RTE <- PC?'")
    typer.echo("and press 'Poursuivre'")

    typer.echo("\n" + "-" * 30)
    flag_start = typer.confirm("Is GP32 ready to receive data ?", default=True)
    if flag_start:
        from_gpx_to_gps(gpx_file)

    typer.echo("\n" + "-" * 30)
    typer.echo("End of program")
    raise typer.Exit()


if __name__ == "__main__":
    app()
