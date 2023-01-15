from telethon import TelegramClient, events
from dotenv import load_dotenv
import logging, os

load_dotenv()

logging.basicConfig(level=logging.WARNING)

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
channel = [os.getenv('channel'), os.getenv('channel2')]
session_name = os.getenv('session_name')

client = TelegramClient(session_name, api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats = channel))
async def main(event):
    print(event.text)    
    # forward event information to discord 
    
client.run_until_disconnected()



