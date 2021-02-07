import random


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