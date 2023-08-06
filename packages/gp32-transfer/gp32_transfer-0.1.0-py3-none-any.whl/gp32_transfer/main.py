import typer
from .typerApp import import_nmea
from .typerApp import write_to_gps

app = typer.Typer()

app.add_typer(import_nmea.app, name="import")
app.add_typer(write_to_gps.app, name="export")


# def main():
#     typer.echo("Hello World")


if __name__ == "__main__":
    app()
