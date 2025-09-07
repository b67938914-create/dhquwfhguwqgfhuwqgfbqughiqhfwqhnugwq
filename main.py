import os

# Bot token - get from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set!")
    print("Please set your Discord bot token in the Replit Secrets tab.")
    exit()

# Import and run the bot
from bot import bot
bot.run(BOT_TOKEN)
