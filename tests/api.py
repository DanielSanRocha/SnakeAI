import json

from aiohttp.client_exceptions import ServerDisconnectedError
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from app.server import main

from config import SCREEN_WIDTH,SCREEN_HEIGHT,GRID_SIZE_X,GRID_SIZE_Y,BACKGROUND_COLOR
from config import BRAIN_LOAD_FILENAME,BRAIN_SAVE_FILENAME,FRAME_RATE,TRAIN_INTERVAL


class HealthCheckOKTestCase(AioHTTPTestCase):
    async def get_application(self):
        app = await main()
        return app

    @unittest_run_loop
    async def test_healthcheck_Ok(self):
        resp = await self.client.get('/healthcheck')
        assert resp.status == 200
        text = await resp.text()
        assert 'WORKING' in text

class PlayTestCase(AioHTTPTestCase):
    async def get_application(self):
        app = await main()
        return app

    @unittest_run_loop
    async def test_healthcheck_Ok(self):
        state = "[[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]]]"
        resp = await self.client.post('/play', data=state)
        assert resp.status == 200
        resp_data = json.loads(await resp.text())
        assert 'control' in resp_data
        assert type(resp_data['control']) == int
        assert resp_data['control'] < 4
        assert resp_data['control'] >= 0

