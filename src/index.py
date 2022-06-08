import discord
from config import token

from app import bot

@bot.event
async def on_ready():
    
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening,
        name="Patricio rey y sus redonditos de ricota")
        )

    print("[BOYLE]: bot has started")

bot.run(token.token)
