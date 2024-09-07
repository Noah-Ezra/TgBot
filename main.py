from pyrogram import Client, filters
from os import getenv


API_ID = "24992766"
API_HASH = "f7f3c0918f653963d8e58c5d6ad54316"
BOT_TOKEN = "6471542930:AAE_fwmRJ0a5uElJxrBoBNoyQ7m5C8eNMjY"


"""
API_ID = getenv('API_ID', False)
API_HASH = getenv('API_HASH', False)
BOT_TOKEN = getenv('BOT_TOKEN', False
"""


ANSHIF = Client(
    name="Anshif81_Bot",
    api_id =API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@ANSHIF.on_message(filters.command("start"))
async def start_cmd(client, message):
    ANSHIF.send_message(message.chat.id, 'test')


@ANSHIF.on_message(filters.command("help"))
async def help_cmd(client, message):
       print("Helps command")



print("Bot started")


if __name__ == '__main__':
  ANSHIF.run()
