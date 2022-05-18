from pyrogram import Client
from pyrogram.errors import FloodWait
from time import sleep

APP_ID = 11542235
API_HASH = "e46bdcd08e7818b6ecc0448446dc7fc3"
SESSION = "AQCwHtsARGXii3QomGF7lirWNnbS8TlplcO_x4NGJIUSIxmlrAHnsopt6CQ_y78eOZLrya_oY2doKY0-HzNlKUqAR0LWJmhpkujr7qRSIlnWL6PrTUCIschKoPWV-MStOQ5qU3dUkcQshE2jDG06KjO7doszlVKe6r8dk6q3mZKs7F8rv-BQMUGh8pqfbpJs5TRLEOw0hdzQI8HnzcIuWC2k7Z54HK4ioN8QVJ6XjW8kZHS9VfZ4cOac9hIzYKwbAmwgdiiGpMceU-OZb-X6zKbPPtShBnPum5m8golJLc2O3KAhXyxHQ-pBFQIEBSOTOZE9xGDQW-6VSzlUeLYLF8O2jwfmLAAAAAE6r_0HAA"

with Client(name='session', api_id=APP_ID, api_hash=API_HASH, session_string=SESSION) as app:
    for message in app.iter_history(-1001766664486, reverse=True):
        try:
            message.copy(-1001627190543)
            sleep(4)
        except Exception as e:
            print(e)
        except FloodWait as er:
            sleep(er.value)
            continue
