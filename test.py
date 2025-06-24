import discord
import requests
import re
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

CHANNEL_ID = 123456789012345678  # Reemplaza con el ID real de tu canal
COIN_REGEX = r'\$([A-Z0-9]{2,10})'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID or message.author.bot:
        return

    match = re.search(COIN_REGEX, message.content)
    if match:
        coin = match.group(1)
        user = message.author.name
        text = f"{user} va a comprar: {coin}"
        print(text)
        send_telegram(text)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

client.run(DISCORD_TOKEN)
