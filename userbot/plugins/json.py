from userbot import devub

from ..core.managers import edit_or_reply
from ..helpers.utils import _format

plugin_devegory = "tools"

# yaml_format is ported from uniborg
@devub.dev_cmd(
    pattern="json$",
    command=("json", plugin_devegory),
    info={
        "header": "To get details of that message in json format.",
        "usage": "{tr}json reply to message",
    },
)
async def _(event):
    "To get details of that message in json format."
    devevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = devevent.stringify()
    await edit_or_reply(event, the_real_message, parse_mode=_format.parse_pre)


@devub.dev_cmd(
    pattern="yaml$",
    command=("yaml", plugin_devegory),
    info={
        "header": "To get details of that message in yaml format.",
        "usage": "{tr}yaml reply to message",
    },
)
async def _(event):
    "To get details of that message in yaml format."
    devevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = _format.yaml_format(devevent)
    await edit_or_reply(event, the_real_message, parse_mode=_format.parse_pre)
