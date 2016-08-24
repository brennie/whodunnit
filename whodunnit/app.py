from aiohttp import web


def create_app(middlewares=None):
    if middlewares is None:
        middlewares = []

    return web.Application(middlewares=middlewares)
