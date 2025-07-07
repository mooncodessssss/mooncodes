import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","18996880"))
API_HASH = getenv("API_HASH","4fbf3bdd35495f210e14b54d4588688d")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","5907277199:AAEbkwvnRPugD5jxbkhE_S-m5U1VBQx0I28")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://moon2:moon2@cluster0.65tjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 200))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1002222604638"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","6391774843"))

# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","mooncodes")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-AAkvMusLkK6RJlWLiEDJqEfDHwpHHNRwWSeZaHdIG6Qg_____wAqt48m8b7K")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mooncodessssss/mooncodes",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHAT", "https://t.me/world_friend_chatting_zone")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/world_friend_chatting_zone")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://files.catbox.moe/jyeumn.jpg")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION","BQFmGd8AIqFMOqBfT8u5KWNrIbto2nzP2I9G0tSRVkBZ2TU6GDFluBB6UnJHRVVfrb22WqsddK6zgmwl0rytBce4W86l5nUwIb9bBesS0g5vkWBBUSGDaE6Jkuq4e2rn0oQj54GHhfuKV5EM1pG0RoKkMBbj-ApHjIKo0NkMwHKdO0-vPQRynup65yKcCyYDoNk2H9OJ6stxvjShTG_yXBKRP_eLEDbdXMaHXjojI2mggt6PuJEY3IGoiqwwjyqoT0ajoefzhNeHC7PGaU5vpBepRcZ_mQymz1TTrx3EugOTp5XG0vXrpzXyi3iMsURsa3tiFUmac7IJ9-ktuNy6O0idwuUAFwAAAAHc8sT8AA")
STRING2 = getenv("STRING_SESSION2","BQFmGd8AORynvhfl4aR5XFUo8rYv2T9Eze1Blddt8xcTY324N_BokkZu-GfN4hCuw4U3_tuWNN63xVvFvMNf7QsSKiY43sB9_eJYYxQKv6dMYDG4kZlTTMi4GANn3V-GInAX4fs_l5oCNBqk1OXaY3ruU5U1ZSFlWApxURRg9VymmMUtgopwI0quPsVUvav4FBfFYPS_MPHlHsa7PZmW8qxYVBpXR0-I8XPQL5TJVHUBCrfANlwm3F_AGgA8jfGjc2BEigda8za5yRRMKDx4UTFwm3VW-QRLFPRhOKpl_vEt7gIh62HOmXHx-oigPeEI5qm-KAo39aK8HCUVHAjv8FQGi9fnCAAAAAFcH-_kAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/k3cw8XS/IMG-20250103-174108-968.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
