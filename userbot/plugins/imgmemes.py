#  Copyright (C) 2020  sandeep.n(π.$)
# credits to @Samarth-Dubey (@samarth1709)
import asyncio
import os
import re

from userbot import devub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_devegory = "fun"


@devub.dev_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_devegory),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs Devuserbot ; One of the Popular userbot",
    },
)
async def nekobot(dev):
    "Fake google search meme"
    text = dev.pattern_match.group(1)
    reply_to_id = await reply_id(dev)
    if not text:
        if dev.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(dev, "`What should i search in google.`", 5)
    deve = await edit_or_reply(dev, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            dev,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    devfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await dev.client.send_file(dev.chat_id, devfile, reply_to=reply_to_id)
    await deve.delete()
    if os.path.exists(devfile):
        os.remove(devfile)


@devub.dev_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_devegory),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump Devuserbot is One of the Popular userbot",
    },
)
async def nekobot(dev):
    "trump tweet sticker with given custom text_"
    text = dev.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(dev)

    reply = await dev.get_reply_message()
    if not text:
        if dev.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(dev, "**Trump : **`What should I tweet`", 5)
    deve = await edit_or_reply(dev, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    devfile = await trumptweet(text)
    await dev.client.send_file(dev.chat_id, devfile, reply_to=reply_to_id)
    await deve.delete()
    if os.path.exists(devfile):
        os.remove(devfile)


@devub.dev_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_devegory),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi Devuserbot is One of the Popular userbot",
    },
)
async def nekobot(dev):
    "modi tweet sticker with given custom text"
    text = dev.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(dev)

    reply = await dev.get_reply_message()
    if not text:
        if dev.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(dev, "**Modi : **`What should I tweet`", 5)
    deve = await edit_or_reply(dev, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    devfile = await moditweet(text)
    await dev.client.send_file(dev.chat_id, devfile, reply_to=reply_to_id)
    await deve.delete()
    if os.path.exists(devfile):
        os.remove(devfile)


@devub.dev_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_devegory),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm Devuserbot is One of the Popular userbot",
    },
)
async def nekobot(dev):
    text = dev.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(dev)

    reply = await dev.get_reply_message()
    if not text:
        if dev.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(dev, "`Give text to write on banner, man`", 5)
    deve = await edit_or_reply(dev, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    devfile = await changemymind(text)
    await dev.client.send_file(dev.chat_id, devfile, reply_to=reply_to_id)
    await deve.delete()
    if os.path.exists(devfile):
        os.remove(devfile)


@devub.dev_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_devegory),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna Devuserbot is One of the Popular userbot",
    },
)
async def nekobot(dev):
    "kanna chan sticker with given custom text"
    text = dev.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(dev)

    reply = await dev.get_reply_message()
    if not text:
        if dev.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(dev, "**Kanna : **`What should i show you`", 5)
    deve = await edit_or_reply(dev, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    devfile = await kannagen(text)
    await dev.client.send_file(dev.chat_id, devfile, reply_to=reply_to_id)
    await deve.delete()
    if os.path.exists(devfile):
        os.remove(devfile)


@devub.dev_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_devegory),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; Devuserbot is One of the Popular userbot",
    },
)
async def nekobot(dev):
    "The desired person tweet sticker with given custom text"
    text = dev.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(dev)

    reply = await dev.get_reply_message()
    if not text:
        if dev.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                dev,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            dev,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    deve = await edit_or_reply(dev, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    devfile = await tweets(text, username)
    await dev.client.send_file(dev.chat_id, devfile, reply_to=reply_to_id)
    await deve.delete()
    if os.path.exists(devfile):
        os.remove(devfile)
