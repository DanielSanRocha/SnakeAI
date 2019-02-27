import logging
import os
    
from aiohttp import web

from app.routes import add_routes

logging.basicConfig(level=logging.DEBUG)

async def main():
    app_server = web.Application()
    add_routes(app_server)

    return app_server

if __name__ == '__main__':
    web.run_app(main(), port=(os.getenv("PORT") or 8000))
