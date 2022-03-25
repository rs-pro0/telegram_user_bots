
from telethon import TelegramClient
from telethon.tl.functions.messages import (
    GetBotCallbackAnswerRequest,
    SendMessageRequest,
    GetHistoryRequest
)
from time import sleep
import asyncio
api_id = 
api_hash = ""
client = TelegramClient("kuku", api_id, api_hash)
client.start()
ltcbot = None
name="channel_name" #you need to be subscribed to channel
user_count=input("User count:")
message=input("Message:")
first_time=input("First time?:")
class LtcBotError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def printError(self):
        print("LtcBotError: ")


async def async_range(count):
    for i in range(count):
        yield(i)
async def work(client):
    if first_time=="1":return
    posts = await client(GetHistoryRequest(
        peer=name,
        limit=1,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))
    post = posts.messages[0]
    while True:
        await client.send_message(entity =name, message=message, comment_to=post)
async def main():
    await asyncio.gather(
       *list(work(TelegramClient('user%d' %(i), api_id, api_hash)) for i in range(int(user_count)))
    )
asyncio.run(main())
