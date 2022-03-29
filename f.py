from pyrogram import Client
from pyrogram.errors import FloodWait
from time import sleep

APP_ID = 11542235
API_HASH = "e46bdcd08e7818b6ecc0448446dc7fc3"
BOT_TOKEN = "5132840587:AAGR_XH1OTqWSVKKre2uBgpaoDrrGAOIT1M"

with Client("pyrogram", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, no_updates=True) as app:
    for message in app.iter_history(-1001673241127, reverse=True):
        try:
            message.copy(-1001655189003)
            sleep(4)
        except Exception as e:
            print(e)
        except FloodWait as er:
            sleep(er.x)
            continue
