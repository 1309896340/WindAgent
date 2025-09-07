from fastapi import FastAPI
from contextlib import asynccontextmanager

from AiAgent.Agent import Client

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.agent = Client()
    print("LLM初始化完成")
    yield
    