import os
import json
import random


def _get_dota2_hero_data():
    data_path = os.path.join(
        os.path.dirname(__file__),
        "dota2_hero_data.json",
    )
    with open(data_path, "r") as datafile:
        return json.load(datafile)

def _get_hero_group(herodata, hero_attr):
    return [
        i["localized_name"] for i in herodata.values() if i["primary_attr"] == hero_attr
    ]

def get_single_draft(*args, **kwargs):
    """
    returns the localized names of 3 heroes in the pool, one per primary attribute.
    """
    herodata = _get_dota2_hero_data()

    str = random.choice(_get_hero_group(herodata, "str"))
    agi = random.choice(_get_hero_group(herodata, "agi"))
    int = random.choice(_get_hero_group(herodata, "int"))
    all = random.choice(_get_hero_group(herodata, "all"))

    r = "```Single Draft: \n" \
        + "              " + str \
        + "\n              " + agi \
        + "\n              " + int \
        + "\n              " + all \
        + "```"

    return r
