import discord
from discord.ext import commands
import asyncio
import ffmpeg  # Nuevo: Uso de ffmpeg-python
from MusicaBot.buscar import search_youtube
from MusicaBot.audio import get_youtube_audio_url

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents().all())
        self.voice_client = None
        self.music_queue = []  # Cola para almacenar las URLs de música
        self.is_playing = False  # Indicador de estado de reproducción

    async def play_music(self, user_id, channel_id, guild_id, query):
        try:
            print(f"Buscando audio para la consulta: {query}")
            guild = self.get_guild(int(guild_id))
            if guild is None:
                print("No se pudo encontrar el servidor.")
                return {"status": "error", "message": "El bot no está en el servidor especificado."}

            member = guild.get_member(int(user_id))
            if member is None:
                print("El usuario no se encuentra en el servidor.")
                return {"status": "error", "message": "El usuario no se encuentra en el servidor."}

            if member.voice is None or member.voice.channel.id != int(channel_id):
                print("El usuario no está en el canal de voz correcto.")
                return {"status": "error", "message": f"El usuario {user_id} no está en el canal de voz correcto."}

            # Buscar y obtener la URL del audio de YouTube
            extract = search_youtube(query)
            url = get_youtube_audio_url(extract)

            if not url:
                raise ValueError("No se pudo obtener la URL del audio.")

            self.music_queue.append(url)
            print(f"Agregada a la cola: {url}. Cola actual: {self.music_queue}")

            if self.voice_client is None:
                self.voice_client = await member.voice.channel.connect()

            if not self.is_playing:
                asyncio.create_task(self.start_playing())

            return {"status": "success", "message": "Canción agregada a la cola", "queue": self.music_queue}

        except Exception as e:
            print(f"Error al reproducir música: {e}")
            return {"status": "error", "message": str(e)}

    async def start_playing(self):
        while self.music_queue:
            url = self.music_queue.pop(0)

            # Opciones de FFmpeg mejoradas
            process = (
                ffmpeg
                .input(url)
                .output('pipe:', format='wav', acodec='pcm_s16le', ac=2, ar='48k')
                .run_async(pipe_stdout=True, pipe_stderr=True)
            )

            self.is_playing = True
            self.voice_client.play(discord.PCMAudio(process.stdout), after=self.check_queue)

            while self.voice_client.is_playing():
                await asyncio.sleep(1)

        if self.voice_client:
            await self.voice_client.disconnect()
            self.voice_client = None
        self.is_playing = False

    def check_queue(self, error=None):
        if error:
            print(f"Error en la reproducción: {error}")
        if self.music_queue:
            asyncio.create_task(self.start_playing())

    async def show_queue(self):
        return self.music_queue

    async def on_ready(self):
        print(f"Bot conectado como {self.user} en el servidor.")

    async def start_bot(self):
        TOKEN = os.getenv("DISCORD_TOKEN")
        await self.start(TOKEN)
