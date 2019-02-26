from aiohttp import web
import asyncio

async def healthcheck(request):
    return web.json_response(data={'status':'WORKING'})
