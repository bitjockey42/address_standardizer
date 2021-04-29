"""Console script for address_standardizer."""
import sys
import click
import pathlib

from address_standardizer.server import start_server
from address_standardizer.utils import (
    process_csv,
    process_csv_alt,
    generate_lookup_map,
    write_json,
    PARENT_DIR,
)
from address_standardizer.settings import HOST, PORT, DEBUG


@click.group()
def main(args=None):
    """Console script for address_standardizer."""
    return 0


@main.command()
@click.argument("filename")
@click.option("-o", "--output-filename", required=False, default=None)
@click.option("-a", "--alt/--no-alt", default=False, help="Use alternate processor")
def update(filename, output_filename, alt):
    """Generate or update the lookup map"""
    if alt:
        processed_rows = process_csv_alt(filename)
    else:
        processed_rows = process_csv(filename)

    lookup_map = generate_lookup_map(processed_rows)

    if output_filename is None:
        output_filename = str(PARENT_DIR.joinpath("data", "lookup_map.json"))

    write_json(lookup_map, output_filename)


@main.command()
@click.option("--host", "-h", required=True, default=HOST)
@click.option("--port", "-p", required=True, default=PORT)
@click.option("--debug/--no-debug", default=True)
def server(host, port, debug):
    """Start the server"""
    start_server(host=host, port=port, debug=debug)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
