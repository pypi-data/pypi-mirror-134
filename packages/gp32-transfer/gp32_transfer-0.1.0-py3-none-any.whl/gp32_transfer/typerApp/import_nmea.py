import typer
from ..utils.serial_util import save_gps_to_gpx

app = typer.Typer()


@app.command()
def save_all(filename: str):
    typer.echo("\n" + "-" * 30)
    typer.echo("Press 'Sauve WP/RTE -> PC?'")
    typer.echo("and press 'Poursuivre'")

    save_gps_to_gpx(filename)


if __name__ == "__main__":
    app()
