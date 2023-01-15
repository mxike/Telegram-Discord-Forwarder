from telethon import TelegramClient, events
from dotenv import load_dotenv
from Message import Message
import logging, os

load_dotenv()

logging.basicConfig(level=logging.WARNING)

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
channel = [os.getenv('channel'), os.getenv('channel2')]
session_name = os.getenv('session_name')

client = TelegramClient(session_name, api_id, api_hash)
client.start()

#discord bot client aanmaken en starten discord_client = DiscordClient()

@client.on(events.NewMessage(chats = channel))
async def main(event):
    message_event = Message(event.message, event.photo)

    print(message_event.get_message())

    if event.photo:
        print("send message + photo") #dit later fixen, eerst discord bot ready maken
        # print(event.photo)
        # message_event.convert_photo()
        # save = await event.download_media()
    
client.run_until_disconnected()

# TODO
# forward event information to discord
# Requirements.txt fixen voor pip install 
# Eerst discord bot maken en de message fixen



