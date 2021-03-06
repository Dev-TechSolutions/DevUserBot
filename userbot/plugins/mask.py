# credits to @Samarth-Dubey and @samarth1709

import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import devub

from ..Config import Config
from ..core.managers import edit_or_reply
from . import awooify, baguette, convert_toimage, iphonex, lolice

plugin_devegory = "extra"


@devub.dev_cmd(
    pattern="mask$",
    command=("mask", plugin_devegory),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(devbot):
    "Hazmat suit maker"
    reply_message = await devbot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await edit_or_reply(devbot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await edit_or_reply(devbot, "```Reply to actual users message.```")
    event = await devbot.edit("```Processing```")
    async with devbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await devbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.edit(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await devbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@devub.dev_cmd(
    pattern="awooify$",
    command=("awooify", plugin_devegory),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def devbot(devmemes):
    "replied Image will be face of other image"
    replied = await devmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    if replied.media:
        devevent = await edit_or_reply(devmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    download_location = await devmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await devevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await devevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await devevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await devevent.edit("ERROR: " + str(exc))
    dev = f"https://telegra.ph{response[0]}"
    dev = await awooify(dev)
    await devevent.delete()
    await devmemes.client.send_file(devmemes.chat_id, dev, reply_to=replied)


@devub.dev_cmd(
    pattern="lolice$",
    command=("lolice", plugin_devegory),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def devbot(devmemes):
    "replied Image will be face of other image"
    replied = await devmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    if replied.media:
        devevent = await edit_or_reply(devmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    download_location = await devmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await devevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await devevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await devevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await devevent.edit("ERROR: " + str(exc))
    dev = f"https://telegra.ph{response[0]}"
    dev = await lolice(dev)
    await devevent.delete()
    await devmemes.client.send_file(devmemes.chat_id, dev, reply_to=replied)


@devub.dev_cmd(
    pattern="bun$",
    command=("bun", plugin_devegory),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def devbot(devmemes):
    "replied Image will be face of other image"
    replied = await devmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    if replied.media:
        devevent = await edit_or_reply(devmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    download_location = await devmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await devevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await devevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await devevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await devevent.edit("ERROR: " + str(exc))
    dev = f"https://telegra.ph{response[0]}"
    dev = await baguette(dev)
    await devevent.delete()
    await devmemes.client.send_file(devmemes.chat_id, dev, reply_to=replied)


@devub.dev_cmd(
    pattern="iphx$",
    command=("iphx", plugin_devegory),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def devbot(devmemes):
    "replied image as iphone x wallpaper."
    replied = await devmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    if replied.media:
        devevent = await edit_or_reply(devmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(devmemes, "reply to a supported media file")
    download_location = await devmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await devevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await devevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await devevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await devevent.edit("ERROR: " + str(exc))
    dev = f"https://telegra.ph{response[0]}"
    dev = await iphonex(dev)
    await devevent.delete()
    await devmemes.client.send_file(devmemes.chat_id, dev, reply_to=replied)
