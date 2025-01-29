import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RessoMusic import LOGGER, app, userbot
from RessoMusic.core.call import AMBOTOP
from RessoMusic.misc import sudo
from RessoMusic.plugins import ALL_MODULES
from RessoMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
import threading
from flask import Flask

# Flask app definition
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "RessoMusic is running on Flask and Thread!"

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RessoMusic.plugins" + all_module)
    LOGGER("RessoMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await AMBOTOP.start()
    try:
        await AMBOTOP.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("RessoMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await AMBOTOP.decorators()
    LOGGER("RessoMusic").info(
        "moon music started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("RessoMusic").info("Stopping AMBOTOP Music Bot...")


def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run the async bot
     asyncio.get_event_loop().run_until_complete(init())
