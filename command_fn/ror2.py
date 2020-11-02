import os
import json
import random


def _get_ror2_data():
    data_path = os.path.join(
        os.path.dirname(__file__),
        "ror2_bot_data.json",
    )
    with open(data_path, "r") as datafile:
        return json.load(datafile)


def get_ror2_equip(*args):
    """
    Roll a random ror2 equipment.
    """
    if args:
        random.seed(str(args))

    return random.choice(_get_ror2_data()["equipments"])

def get_ror2_char(*args):
    """
    Roll a random ror2 character.
    """
    if args:
        random.seed(str(args))

    return random.choice(_get_ror2_data()["characters"])

def get_ror2_build(*args):
    """
    Roll a random ror2 build.
    """
    ror2_builds = _get_ror2_data()["builds"]
    ror2_characters = _get_ror2_data()["characters"]

    c = False
    if args:
        for s in ror2_characters:
            if s.lower() == args[0].lower():
                c = s
                break
    
    if c:
        b = random.choice([k for k,v in ror2_builds.items() if not v["character"] or c in v["character"]])
    else:
        b = random.choice(list(ror2_builds.keys()))
        if ror2_builds[b]["character"]:
            c = random.choice(ror2_builds[b]["character"])
        else:
            c = random.choice(ror2_characters)

    return "Character: " + c + "\nBuild: " + ror2_builds[b]["name"]
