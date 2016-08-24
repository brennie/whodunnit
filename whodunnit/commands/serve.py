import click
from aiohttp import web

from whodunnit.app import app


@click.command()
def main():
    web.run_app(app)


if __name__ == '__main__':
    main()
