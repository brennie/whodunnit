import click
from aiohttp import web

from whodunnit.app import create_app


@click.command()
def main():
    app = create_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
