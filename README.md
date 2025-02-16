# Bienvenido a la API de BDFD [REPRODUCTOR DE MUSICA]

BDFD (Bot Designer for Discord) permite a los desarrolladores crear bots personalizados para Discord sin necesidad de programación avanzada. 


## MODIFICACIONES

En cualquier diploy render, vercelapp o cualquiera establece las variable de entorno, esta variable de entorno tiene que tener como valor el token de tu bot de discord y como nombre `"DISCORD_TOKEN"`, de preferencia elige [Railway](https://railway.com) como HOST gratuito

## TUTORIALES

**Repositorio**

Como obtener el repositorio en tu perfil [click aqui..](https://streamable.com/1gigfp)

**Host Gratis**

Como desplegar el repositorio en Railway [click aqui..](https://streamable.com/9qtqhr)

**BDFD**

Basic
```python
$var[json;{"user_id": "$authorID",
    "channel_id": "$channelID",
    "guild_id": "$guildID",
    "query": "company justin bieber"}]

$httpPost[YOUR URL HOST/play-music;$var[json]]
$httpResult
```

Advanced

```
$nomention
$var[n;$message]

$var[URL;YOUR URL RAILAPP]

$var[json;{"user_id": "$authorID",
    "channel_id": "$channelID",
    "guild_id": "$guildID",
    "query": "$message"}]
    
$httpPost[$var[URL]/play-music;$var[json]]


$jsonParse[$httpResult]

$thumbnail[$json[message;info_music;videos;0;thumbnails;0]]
$title[$json[message;info_music;videos;0;title]]
$var[desc;$json[message;info_music;videos;0;long_desc]]

$description[$replaceText[$replaceText[$checkCondition[$var[desc]==null];true;Ninguna descripcion;1];false;$var[desc];1]]

$addField[Canal;$json[message;info_music;videos;0;channel];true]
$addField[Duracion;`$json[message;info_music;videos;0;duration]`;false]
$addField[Vistas;`$json[message;info_music;videos;0;views]`;true]
$addField[Publicado;`$json[message;info_music;videos;0;publish_time]`;false]

$addField[Youtube video;[Link..\](https://www.youtube.com$json[message;info_music;videos;0;url_suffix]);false]
$color[$random[000000;999999]]

```
## ERRORES

**COOKIES**

En caso de errores de cookies, que despues de unos dias los cookies de este repositorio no funcionara, edita el archivo de [cookies.txt](https://github.com/IzanaonYT/bdfd-music-2025-/blob/main/cookies.txt), y sigue el siguiente tutorial.

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




