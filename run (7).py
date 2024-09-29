from highrise.__main__ import *
from importlib import import_module
import time
import asyncio
import traceback
from keep_alive import keep_alive
import os

bot_file_name = "mybot"
bot_class_name = "MyBot"
room_id = "656eb5d50bd29fb70deb5508"
bot_token = "2d590a4808e497b364f0acbc02e517d40d2509af1804dc6667cffd9b9ea21012"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

# Start the Flask server to keep the bot alive
keep_alive()

async def run_bot():
    while True:
        try:
            definitions = [my_bot]
            await main(definitions)
        except Exception as e:
            traceback.print_exc()  # Print the full traceback of the exception
            print(f"An exception occurred: {e}")
            time.sleep(5)
        finally:
            print("Bot has stopped. Restarting in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    # Check if the watchdog script is not running
    if not os.environ.get("REPL_WATCHDOG"):
        asyncio.run(run_bot())  # Run the bot
