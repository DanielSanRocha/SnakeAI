import aiohttp_cors
from aiohttp import web

from app.controllers.healthcheck import healthcheck
from app.controllers.play import play

def add_routes(app):
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    resource = cors.add(app.router.add_resource("/play"))
    cors.add(resource.add_route("POST", play))

    app.router.add_route("GET", "/healthcheck", healthcheck)
