import nekos

from userbot import devub

from ..core.managers import edit_or_reply

plugin_devegory = "fun"


@devub.dev_cmd(
    pattern="tdev$",
    command=("tdev", plugin_devegory),
    info={
        "header": "Some random dev facial text art",
        "usage": "{tr}tdev",
    },
)
async def hmm(dev):
    "Some random dev facial text art"
    reactdev = nekos.textdev()
    await edit_or_reply(dev, reactdev)


@devub.dev_cmd(
    pattern="why$",
    command=("why", plugin_devegory),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(dev):
    "Some random Funny questions"
    whydev = nekos.why()
    await edit_or_reply(dev, whydev)


@devub.dev_cmd(
    pattern="fact$",
    command=("fact", plugin_devegory),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(dev):
    "Some random facts"
    factdev = nekos.fact()
    await edit_or_reply(dev, factdev)
