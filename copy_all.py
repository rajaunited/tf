from time import sleep
from pyrogram import Client
from pyrogram.errors import FloodWait
from logging import error

APP_ID = 11542235
API_HASH = "e46bdcd08e7818b6ecc0448446dc7fc3"
SESSION = "AQAaCgStFBP_a60gMmg4TlUT1OFmqdFcVIhTY_1ANfci5Cc4pPYO9_2FStxhufXij9p2oLYmDteHhobwa13L_9zFcWTLsA2AZ4jhDOrho8wE00h8gO5wDuAzSteTPdw9ITNq6IVOQGeWCyI0q8AavBTsv96Iv30-RVyuwF_ZLRT3zIKsOQ2_ibjONAFPsnq3fzXrUTSJqHRr-DbobJW5V2D4mijrXP6G7KXwtLdbq-ONb9eWYnRoQgAnoXv7Eb18aNfeCFKyYNtDqZaj38Fa_UQlUiN8CPkswD3MXszTNJKcBku71UXRxhIL4ER-p__hP6RUPnuAbDGGBJMJsR3vBwVPAAAAATqv_QcA"

with Client(SESSION, api_id=APP_ID, api_hash=API_HASH) as app:
    for message in app.iter_history(-1001277293346, reverse=True):
        try:
            message.copy(-1001701282526)
            print(f"Sussesfuly Copied Message Id: {message.message_id}")
            sleep(4)
        except Exception as e:
            error(e)
        except FloodWait as er:
            error(er)
            sleep(er.x)
            continue
