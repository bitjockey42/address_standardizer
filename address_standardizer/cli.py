"""Console script for address_standardizer."""
import sys
import click
import pathlib

from address_standardizer.server import start_server
from address_standardizer.utils import generate_lookup_map, write_json, PARENT_DIR


@click.group()
def main(args=None):
    """Console script for address_standardizer."""
    return 0


@main.command()
@click.argument("filename")
@click.option("-o", "--output-filename", required=False, default=None)
def update(filename, output_filename):
    """Generate or update the lookup map"""
    lookup_map = generate_lookup_map(filename)

    if output_filename is None:
        output_filename = str(PARENT_DIR.joinpath("data", "lookup_map.json"))

    write_json(lookup_map, output_filename)


@main.command()
@click.option("--host", "-h", required=True, default="0.0.0.0")
@click.option("--port", "-p", required=True, default="8080")
@click.option("--debug/--no-debug", default=True)
def server(host, port, debug):
    """Start the server"""
    start_server(host=host, port=port, debug=debug)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
