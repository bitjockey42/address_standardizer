"""Console script for address_standardizer."""
import sys

import click


@click.group()
def main(args=None):
    """Console script for address_standardizer."""
    return 0


@main.command()
@click.argument("filename")
def update(filename):
    """Generate or update the lookup map"""
    click.echo("Update")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
