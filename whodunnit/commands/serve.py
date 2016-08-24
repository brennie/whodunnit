import os

import click
import yaml
from aiohttp import web
from aiohttp_index import IndexMiddleware

from whodunnit.app import create_app


@click.command()
@click.option('--development', is_flag=True,
              help='Run a development server instead of a production server.')
def main(development):
    """Run the whodunnit server."""
    with open('whodunnit.yml') as f:
        config = yaml.load(f)

    middlewares = []

    if development:
        host = 'localhost'
        middlewares.append(IndexMiddleware())
    else:
        host = config['host']

    app = create_app(middlewares=middlewares)

    if development:
        static_root = os.path.join(os.path.dirname(__file__), '..', 'htdocs')
        app.router.add_static('/', static_root)

    web.run_app(app, host=host, port=config['port'])


if __name__ == '__main__':
    main()
