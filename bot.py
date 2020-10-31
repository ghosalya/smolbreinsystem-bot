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

def roll_dice(*args):
    """
    Roll a dice. `$dice` rolls a d6, `$dice X` rolls a dX, and `$dice X Y` rolls between X and Y.
    """
    try:
        if len(args) == 0:
            # roll d6
            return random.randint(1, 6)

        if len(args) == 1:
            # roll d*
            return random.randint(1, int(args[0]))

        else:
            return random.randint(int(args[0]), int(args[1]))
    except Exception as e:
        return "Can't roll dice: " + str(e)


def get_ror2_equip(*args):
    """
    Roll a random ror2 equipment.
    """
    if args:
        random.seed(str(args))

    return random.choice([
        "Disposable Missile Launcher",
        "Foreign Fruit",
        "Primordial Cube",
        "Ocular HUD",
        "The Back-Up",
        "Preon Accumulator",
        "Milky Chrysalis",
        "Royal Capacitor",
        "The Crowdfunder",
        "Gnarled Woodsprite",
        "Radar Scanner",
        "Eccentric Vase",
        "Volcanic Egg",
        "Jade Elephant",
    ])


COMMANDS = {
    "$cowgames": get_cow_games,
    "$advice": get_advice,
    "$dice": roll_dice,
    "$ror2equip": get_ror2_equip,
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