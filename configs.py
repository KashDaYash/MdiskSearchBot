# (c) @KashDaYash

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

๐ค My Name: <a href='https://t.me/DynicaBots'>Mdisk Search Robot</a>

๐ Language : <a href='https://www.python.org'> Python V3</a>

๐ Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

๐ก Server: <a href='https://heroku.com'>Heroku</a>

๐จโ๐ป Created By: <a href='https://t.me/KashDaYash'>YK๐ฎ๐ณ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>๐จโ๐ป Developer : <a href='https://t.me/DynicaBots'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}๐,

I'm Mdisk Search Robot.๐ค</a>

I Can Search ๐ What You Wantโ

<a>Made With โค By @@ynicaBots</a></b>
"""


    START_MSG = """
<b>Hey! {}๐,

I'm Mdisk Search Robot.๐ค</a>

I Can Search ๐ What You Wantโ

<a>Made With โค By @DynicaBots</a></b>
"""


