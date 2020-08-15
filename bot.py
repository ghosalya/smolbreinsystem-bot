# bot.py
# from https://realpython.com/how-to-make-a-discord-bot-python/
import os

import discord
import random
import inspect
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

def get_cow_games(*args):
    """
    Suggests a game to play.
    """
    if args:
        random.seed(str(args))

    return random.choice([
        "Let's play: Borderlands 3",
        "Let's play: Stardew Valley",
        "Let's play: Risk of Rain 2",
        "Let's play: Destiny 2",
        "Let's play: Jackbox",
        "Let's play: Scribbl.io",
        "Let's play: Towerfall",
        "Let's play: Alien Swarm",
        "Let's play: HTHT",
    ])

def get_advice(*args):
    """
    Get advice on your problem.
    """
    if args:
        random.seed(str(args))

    return random.choice([
        "The system recommends: git gud",
        "The system recommends: reach superior positioning",
        "The system recommends: follow the supreme leader",
        "The system recommends: blame fireteam leader",
        "The system recommends: chill, there's nothing to lose",
    ])

COMMANDS = {
    "$cowgames": get_cow_games,
    "$advice": get_advice,
}

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

    message_command = message.content.split(" ")[0]
    if message_command in COMMANDS:
        args = message.content.split(" ")[1:]
        response = COMMANDS[message_command](*args)
        await message.channel.send(response)

client.run(TOKEN)