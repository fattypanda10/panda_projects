from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from helper_funcs import get_html

html = get_html("index.html")
app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json(data)
