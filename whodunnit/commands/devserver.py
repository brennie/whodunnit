import os

import click
from aiohttp import web
from aiohttp_index import IndexMiddleware

from whodunnit.app import create_app


@click.command()
def main():
    static_root = os.path.join(os.path.dirname(__file__), '..', 'htdocs')
    app = create_app(middlewares=[IndexMiddleware()])
    app.router.add_static('/', static_root)
    web.run_app(app)


if __name__ == '__main__':
    main()
