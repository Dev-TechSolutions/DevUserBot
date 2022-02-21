import random

from telethon.errors.rpcbaseerrors import ForbiddenError
from telethon.errors.rpcerrorlist import PollOptionInvalidError
from telethon.tl.types import InputMediaPoll, Poll

from userbot import devub

from ..core.managers import edit_or_reply
from . import Build_Poll, reply_id

plugin_devegory = "extra"


@devub.dev_cmd(
    pattern="poll(?:\s|$)([\s\S]*)",
    command=("poll", plugin_devegory),
    info={
        "header": "To create a poll.",
        "description": "If you doesnt give any input it sends a default poll",
        "usage": ["{tr}poll", "{tr}poll question ; option 1; option2"],
        "examples": "{tr}poll Are you an early bird or a night owl ;Early bird ; Night owl",
    },
)
async def pollcreator(devpoll):
    "To create a poll"
    reply_to_id = await reply_id(devpoll)
    string = "".join(devpoll.text.split(maxsplit=1)[1:])
    if not string:
        options = Build_Poll(["Yah sure 😊✌️", "Nah 😏😕", "Whatever die sur 🥱🙄"])
        try:
            await devpoll.client.send_message(
                devpoll.chat_id,
                file=InputMediaPoll(
                    poll=Poll(
                        id=random.getrandbits(32),
                        question="👆👆So do you guys agree with this?",
                        answers=options,
                    )
                ),
                reply_to=reply_to_id,
            )
            await devpoll.delete()
        except PollOptionInvalidError:
            await edit_or_reply(
                devpoll, "`A poll option used invalid data (the data may be too long).`"
            )
        except ForbiddenError:
            await edit_or_reply(devpoll, "`This chat has forbidden the polls`")
        except exception as e:
            await edit_or_reply(devpoll, str(e))
    else:
        devinput = string.split(";")
        if len(devinput) > 2 and len(devinput) < 12:
            options = Build_Poll(devinput[1:])
            try:
                await devpoll.client.send_message(
                    devpoll.chat_id,
                    file=InputMediaPoll(
                        poll=Poll(
                            id=random.getrandbits(32),
                            question=devinput[0],
                            answers=options,
                        )
                    ),
                    reply_to=reply_to_id,
                )
                await devpoll.delete()
            except PollOptionInvalidError:
                await edit_or_reply(
                    devpoll,
                    "`A poll option used invalid data (the data may be too long).`",
                )
            except ForbiddenError:
                await edit_or_reply(devpoll, "`This chat has forbidden the polls`")
            except Exception as e:
                await edit_or_reply(devpoll, str(e))
        else:
            await edit_or_reply(
                devpoll,
                "Make sure that you used Correct syntax `.poll question ; option1 ; option2`",
            )
