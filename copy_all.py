from time import sleep
from pyrogram import Client
from pyrogram.errors import FloodWait

APP_ID = 14985580
API_HASH = "91e12775f7841ca784b463070df7dcbe"
SESSION = "AQByqgDJnaePmzWdK8ppEioGPfeEW19PsdGlF8Fqt2ljcnPcmnyOT0CuhwH3MSKdXKpqUKFPQBTVPv7NGhggHH3gIsVRUznG_C4O2bOiSDAqJtTdUoYXPhsmW7QVV0Cbs3rpoe5iOShb7o6Uv35txKa1QYbj0hXz4uJQsbY5YvIJRWPsl008eb_ZHZ"

with Client(SESSION, api_id=APP_ID, api_hash=API_HASH) as app:
    for message in app.iter_history(-1001277293346, reverse=True):
        try:
            message.copy(-1001638881016)
            print(f"Sussesfuly Copied Message Id: {message.message_id}")
            sleep(4)
        except FloodWait as e:
            print(e)
            sleep(e.x)
        except Exception as er:
            print(er)
            continue
