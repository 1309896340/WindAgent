from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from backend.Schema import Param
from backend.Initializer import lifespan


app = FastAPI(title="Wind Ai大模型", debug=True, lifespan=lifespan)
app.add_middleware(CORSMiddleware,
    allow_origins=['http://127.0.0.1:5173','http://localhost:5173','http://127.0.0.1:8000','http://localhost:8000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'] 
)

@app.post('/')
async def request_llm(param: Param):
    responses = app.state.agent.request(param.question)
    return StreamingResponse(responses, media_type='text/plain')
