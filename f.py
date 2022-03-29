from pyrogram import Client
from pyrogram.errors import FloodWait
from time import sleep

APP_ID = 11542235
API_HASH = "e46bdcd08e7818b6ecc0448446dc7fc3"
SESSION = "AQCUnruvWXOjaOstcF-G_HaObzD1LYFs1GI_J4EZs6vq_dQttJUKk-ReMfL8iJogIx4XoPGQpwyeXU_U7lurhbAT4b87cIz0qdCkIFgsriaB2B1X5g3Rk1uorLitTPqKt6zC7rXOnviyz6p6Z1Mdl_IkAqKOlmw0JzgIGLhsZVWdP8nryC3Znngv2KJ6i5ruValF4dkhdAXpZ2OkrSIn1TLwSDTPvrIjCUZZiSrN8EcL2HtGvfx_fUiZjEoGK00r7oJ1CoXelyIhgcEkNow3wUdH9EQ1OtCmYtMPykPvjWZeKT8Y3mBXpDTuJ7YxqtKD0LevwYmgYRrgTv-FPk8SfMnsAAAAATfMwVAA"

with Client(SESSION, api_id=APP_ID, api_hash=API_HASH) as app:
    for message in app.iter_history(-1001673241127, reverse=True):
        try:
            message.copy(-1001655189003)
            sleep(4)
        except Exception as e:
            print(e)
        except FloodWait as er:
            sleep(er.x)
            continue
