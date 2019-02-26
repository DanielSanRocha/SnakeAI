import logging
import os
    
from aiohttp import web
from app.routes import ROUTES

logging.basicConfig(level=logging.DEBUG)

async def main():
    app_server = web.Application()
    app_server.add_routes(ROUTES)
    return app_server

if __name__ == '__main__':
    web.run_app(main(), port=(os.getenv("PORT") or 8000))
