from telethon import TelegramClient, events
from dotenv import load_dotenv
from Message import Message
from DiscordBot import DiscordWebhookForwarder
import logging, os

load_dotenv()

logging.basicConfig(level=logging.WARNING)

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
channel = [os.getenv('channel'), os.getenv('channel2')]
session_name = os.getenv('session_name')
webhook_url = os.getenv('discord_webhook_url')

client = TelegramClient(session_name, api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats = channel))
async def main(event):
    message_event = Message(event.message, event.photo)
    to_discord = DiscordWebhookForwarder(webhook_url)

    to_discord.send_message(message_event.get_message())

    if event.photo:
        # print("send message + photo", event.photo, event.photo.sizes[0].bytes)
        pass

client.run_until_disconnected()

# TODO
# Requirements.txt fixen voor pip install 
# Make Readme
# Fix incoming photo's and forward them 


