"""Console script for address_standardizer."""
import sys
import click
import pathlib

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


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
