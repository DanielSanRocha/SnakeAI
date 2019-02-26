from aiohttp import web

from app.controllers.healthcheck import healthcheck
from app.controllers.play import play

ROUTES = [
        web.get('/healthcheck', healthcheck),
        web.post('/play', play)
    ]
