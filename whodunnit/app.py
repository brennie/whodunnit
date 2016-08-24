from aiohttp import web


async def handle(request):
    return web.Response(body=b'')


app = web.Application()
app.router.add_route('GET', '/', handle, name='root')
