import signal
import sys
import time

import heroku3

from .Config import Config
from .core.logger import logging
from .core.session import devub
from .helpers.utils.utils import runasync
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "3.0"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "DevUserBot <https://github.com/Samarth-Dubey/DevUserBot>"
__copyright__ = f"DevUserBot Copyright (C) 2021 - 2022  {__author__}"

devub.version = __version__
devub.tgbot.version = __version__
LOGS = logging.getLogger("DevUserbot")
bot = devub

StartTime = time.time()
devversion = "3.0"


def close_connection(*_):
    print("Clossing Userbot connection.")
    runasync(devub.disconnect())
    sys.exit(143)


signal.signal(signal.SIGTERM, close_connection)

if Config.UPSTREAM_REPO == "https://github.com/Samarth-Dubey/DevUserBot":
    UPSTREAM_REPO_URL = "https://github.com/Samarth-Dubey/DevUserBot"
elif Config.UPSTREAM_REPO == "https://github.com/Samarth-Dubey/DevUserBot":
    UPSTREAM_REPO_URL = "https://github.com/Samarth-Dubey/DevUserBot"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID
