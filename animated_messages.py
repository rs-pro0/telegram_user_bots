from telethon import TelegramClient, events
import copy
from time import sleep
from telethon import errors

api_id = TGAPIID
api_hash = TGAPIHASH
client = TelegramClient("kuku", api_id, api_hash)


@client.on(events.NewMessage(outgoing=True))
async def my_event_handler(msg):
    if msg.raw_text.startswith(".type "):
        orig_text = msg.text.split(".type ", maxsplit=1)[1]
    elif msg.raw_text.startswith(".пиши "):
        orig_text = msg.text.split(".пиши ", maxsplit=1)[1]
    else:
        return
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while tbp != orig_text:
        try:
            msg = await msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg = await msg.edit(tbp)
            sleep(0.05)

        except errors.FloodWaitError as e:
            sleep(e.seconds)


client.start()
client.run_until_disconnected()
