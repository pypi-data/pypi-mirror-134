import click
from pathlib import Path

import pynumbat

from pynumbat import current_location
from pynumbat import create_basic_config


@click.command()
@click.option('--path', '-p', default=current_location)
@click.option('--force', '-f', default=False)
@click.option('--virtual', '-v', default=True)
@click.option('--upload', '-u', default=False)
def main(path, force, virtual, upload):
    create_basic_config(Path(path), force, virtual, upload)


if __name__ == '__main__':
    main()