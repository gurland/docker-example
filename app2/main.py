from aiohttp import web


async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/webhook2', hello)])
web.run_app(app, port=80)

