from pyrogram import Client
from pyrogram.errors import FloodWait
from time import sleep

APP_ID = 11542235
API_HASH = "e46bdcd08e7818b6ecc0448446dc7fc3"

with Client("AQCV4qDYBrczVFi7PNuuWntoXInA6b9-7HIWSQpR0Mio6Bce7ZGYx4lPnYGkQVUs8ePmiTwlwWJuE1v-1tI_rEt25WrA1u-06EFAPMwkJb4QSgLVUwHQdVVZ0CMT2117PLWATuBCcXPEL69vi0dAHuRBV-OB1mKhvtBc6cqd9xjUalV3-LbX_N-axueNSQ-AsGiO7SiSTCBco4bNrfufzomEbA6m5MurhYm9tnOgwFANWRGKPdg1g3Y6w_oNuVDQe8zIJvTSY3YjJkY2rm-rP25RoHahs9FcfanyWZA1LL-kA8f-TQlLyriFlxunej9ASVaEMgN8mWsjjvu4YzGmrD85AAAAATUChCAA", api_id=APP_ID, api_hash=API_HASH) as app:
    for message in app.iter_history(-1001673241127, reverse=True):
        try:
            message.copy(-1001655189003)
            sleep(1)
        except FloodWait as e:
            sleep(e.x)
            pass
