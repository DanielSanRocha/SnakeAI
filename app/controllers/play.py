import json
import logging

from aiohttp import web

from agent import Agent
from config import GRID_SIZE_X,GRID_SIZE_Y
from config import BRAIN_LOAD_FILENAME

import ast

class AgentAPI():
    def __init__(self, *args, **kwargs):
        self.agent = Agent(GRID_SIZE_X,GRID_SIZE_Y,4)
        if(BRAIN_LOAD_FILENAME):
            self.agent.loadNeuralNetwork(BRAIN_LOAD_FILENAME)
        else:
            raise Exception("No Brain filename specified!")

    async def play(self, state):
        control = self.agent.predict(state)
        return {"control": int(control)}

agentAPI = AgentAPI()

async def play(request):
    body = await request.read()
    state = ast.literal_eval(body.decode("utf-8"))
    response = await agentAPI.play(state)
    return web.json_response(response)