import nextcord
import os
from dotenv import load_dotenv, find_dotenv
from nextcord.ext import commands
from config import *

def main():
    intents = nextcord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    # temp = dotenv_values(".env")
    load_dotenv(find_dotenv())
    
    @bot.event
    async def on_ready():
        print("Rocketry Bot is Online")
    
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            bot.load_extension(f"modules.{folder}.cog")

    bot.run(BOT_TOKEN)

if __name__ == '__main__':
    main()