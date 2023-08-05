import sys

import click
from flake8_codes import _cli as c


@click.command(
    no_args_is_help=True,
)
@click.argument("code")
def cli(code):
    c.print_codes(code.upper().strip(), sys.stdout)
