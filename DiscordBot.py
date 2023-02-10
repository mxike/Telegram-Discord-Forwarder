from discord_webhook import DiscordWebhook, DiscordEmbed

class DiscordWebhookForwarder():
    def __init__(self, url):
        self.url = url

    def send_message(self, message):
        return DiscordWebhook(url=self.url, content=message).execute()
    
    def send_photo(self, photo):
        webhook = DiscordWebhook(url=self.url)
        embed = DiscordEmbed().set_image(photo)
        webhook.add_embed(embed)
        return webhook.execute()
    
    def send_photo_message(self, message, photo):
        pass
