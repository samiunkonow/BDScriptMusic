from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from bot import MusicBot
import asyncio
import os
from dotenv import load_dotenv
import uvicorn

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI()

# Diccionario para almacenar bots por session_id
active_bots = {}

class MusicRequest(BaseModel):
    user_id: str
    channel_id: str
    guild_id: str
    query: str
    session_id: str
    token: str

@app.on_event("startup")
async def startup_event():
    # Inicia los bots de Discord cuando la aplicación arranca (si es necesario)
    pass

@app.post("/start-bot")
async def start_bot(request: MusicRequest):
    try:
        # Si no hay un bot para esta session_id, crea uno nuevo
        if request.session_id not in active_bots:
            music_bot = MusicBot(token=request.token)
            active_bots[request.session_id] = music_bot
            asyncio.create_task(music_bot.start_bot())
            return JSONResponse({"message": "Bot iniciado correctamente"}, status_code=200)
        return JSONResponse({"message": "Bot ya está en ejecución"}, status_code=400)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/play-music")
async def play_music(request: MusicRequest):
    try:
        # Verifica si el bot ya está corriendo para esta session_id
        if request.session_id not in active_bots:
            raise HTTPException(status_code=400, detail="Bot no está en ejecución")

        music_bot = active_bots[request.session_id]
        m = await music_bot.play_music(request.user_id, request.channel_id, request.guild_id, request.query)
        return JSONResponse({"message": m}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/music-queue")
async def music_queue(session_id: str):
    try:
        # Verifica si el bot está corriendo para esta session_id
        if session_id not in active_bots:
            raise HTTPException(status_code=400, detail="Bot no está en ejecución")

        music_bot = active_bots[session_id]
        queue = await music_bot.show_queue()
        return {"queue": queue}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


