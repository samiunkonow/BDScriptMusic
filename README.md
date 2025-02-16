# Bienvenido a la API de BDFD [REPRODUCTOR DE MUSICA]

BDFD (Bot Designer for Discord) permite a los desarrolladores crear bots personalizados para Discord sin necesidad de programación avanzada. 


## MODIFICACIONES

En cualquier diploy render, vercelapp o cualquiera establece las variable de entorno, esta variable de entorno tiene que tener como valor el token de tu bot de discord y como nombre `"DISCORD_TOKEN"`, de preferencia elige [Railway](https://railway.com) como HOST gratuito

## TUTORIALES

Como obtener el repositorio en tu perfil [click aqui..](https://streamable.com/1gigfp)

Como desplegar el repositorio en Railway [click aqui..](https://streamable.com/9qtqhr)

**BDFD**

```python


$var[json;{"user_id": "$authorID",
    "channel_id": "$channelID",
    "guild_id": "$guildID",
    "query": "company justin bieber"}]

$httpPost[YOUR URL HOST/play-music;$var[json]]
$httpResult```


## ERRORES

**COOKIES**

En caso de errores de cookies, edita el archivo de [cookies.txt](https://github.com/IzanaonYT/bdfd-music-2025-/blob/main/cookies.txt), y seguie el siguiente tutorial.

- Agrega la extensión [Get cookies.txt](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)  en tu navegador LOCALMENTE
- Haz clic derecho en el ícono de la extensión y haz clic en "Administrar extensión"
- Habilita "Permitir en modo incógnito"
- Abre una ventana de incógnito
- Ve a https://youtube.com/
- Inicia sesión
- Cuando estés nuevamente en la página principal de YouTube, luego de iniciar sesión, en la esquina estara el icono de la extension dale click
- Haz clic en "Exportar todas las cookies"
- Copia el contenido del archivo y pegalo en archivo de cookies en el repositorio


**BOT DE DISCORD**

Ayuda especial en el [Servidor de Soporte](https://discord.gg/aP27xXeAsS)

**BDFD**

Ayuda especial en el [Servidor de Soporte](https://discord.gg/aP27xXeAsS)




