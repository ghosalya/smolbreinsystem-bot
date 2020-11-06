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


def _get_acronym(string):
    string_tokens = string.lower().split(" ")
    return "".join([token[0] for token in string_tokens])


def get_ror2_equip(*args):
    """
    Roll a random ror2 equipment. If an equipment name is provided, returns a recommended number of fuel cells.
    """
    ror2_equipments = _get_ror2_data()["equipments"]
    e = False
    if args:
        for s in ror2_equipments.keys():
            if s.lower() == args[0].lower():
                e = s
                break
            # also check for acronyms
            if _get_acronym(s) == args[0].lower():
                e = s
                break

    else:
        e = random.choice(list(ror2_equipments.keys()))
    
    r = "Equipment: " + e
    fc = ror2_equipments[e]
    try:
        iterator = iter(fc)
        r = r + "\nFuel cell breakpoints: " + ', '.join([str(a) for a in fc])
        return r
    except:
        if fc > 0:
            return r + "\nFuel cells for permanent uptime: " + str(fc)
        else:
            return r

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
