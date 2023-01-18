from discord_webhook import DiscordWebhook

class DiscordWebhookForwarder():
    def __init__(self, url):
        self.url = url

    def send_message(self, message):
        return DiscordWebhook(url=self.url, content=message).execute()
    
    def send_message(self, message, photo):
        pass
