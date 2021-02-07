import random


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
