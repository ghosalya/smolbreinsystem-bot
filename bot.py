# bot.py
# from https://realpython.com/how-to-make-a-discord-bot-python/
import os

import discord
import random
import inspect
from dotenv import load_dotenv

from command_fn.generic import roll_dice
from command_fn.cows import get_advice, get_cow_games
from command_fn.ror2 import (
    get_ror2_build,
    get_ror2_char,
    get_ror2_equip,
)
from command_fn.genshin import ehe


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

COMMANDS = {
    "$cowgames": get_cow_games,
    "$advice": get_advice,
    "$dice": roll_dice,
    "$ror2equip": get_ror2_equip,
    "$ror2char": get_ror2_char,
    "$ror2build": get_ror2_build,
    "ehe": ehe,
}

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

def help():
    return "\n".join([
        f"`{name}` - {inspect.getdoc(fn)}"
        for name, fn in COMMANDS.items()
    ])

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$help":
        await message.channel.send(help())

    message_command = message.content.split(" ")[0].lower()
    if message_command in COMMANDS:
        args = message.content.split(" ")[1:]
        response = COMMANDS[message_command](*args)
        await message.channel.send(response)


if __name__ == "__main__":
    client.run(TOKEN)
