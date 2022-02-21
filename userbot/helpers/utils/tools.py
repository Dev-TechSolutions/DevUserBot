import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        devevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        devevent = event
    devmedia = None
    devfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(devfile):
        os.remove(devfile)
    if mediatype == "Photo":
        devmedia = await reply.download_media(file="./temp")
        im = Image.open(devmedia)
        im.save(devfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, devfile, thumb=-1)
    elif mediatype == "Sticker":
        devmedia = await reply.download_media(file="./temp")
        if devmedia.endswith(".tgs"):
            devcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{devmedia}' '{devfile}'"
            stdout, stderr = (await runcmd(devcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif devmedia.endswith(".webp"):
            im = Image.open(devmedia)
            im.save(devfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, devfile, thumb=-1)
        if not os.path.exists(devfile):
            devmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(devfile, 0.1)
            except Exception:
                clip = clip.save_frame(devfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            devmedia = await reply.download_media(file="./temp")
            im = Image.open(devmedia)
            im.save(devfile)
    if devmedia and os.path.lexists(devmedia):
        os.remove(devmedia)
    if os.path.lexists(devfile):
        return devevent, devfile, mediatype
    return devevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
