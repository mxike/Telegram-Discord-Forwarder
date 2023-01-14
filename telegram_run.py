from telethon import TelegramClient, events
import logging

logging.basicConfig(level=logging.WARNING)

api_id = 12345
api_hash = ''
channel = [""]
session_name = ''

client = TelegramClient(session_name, api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats = channel))
async def main(event):
    print(event.text)    
    # forward event information to discord 
    
client.run_until_disconnected()



