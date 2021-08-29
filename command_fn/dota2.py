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

def get_single_draft(*args):
    """
    returns the localized names of 3 heroes in the pool, one per primary attribute.
    """
    herodata = _get_dota2_hero_data()

    str = random.choice([i.value.localized_name for i in herodata if i.value.primary_attr == "str"])
    agi = random.choice([i.value.localized_name for i in herodata if i.value.primary_attr == "agi"])
    int = random.choice([i.value.localized_name for i in herodata if i.value.primary_attr == "int"])

    r = "```Single Draft: " + str \
        + "\n              " + agi \
        + "\n              " + int \
        + "```"

    return r
