from bot import roll_dice


def test_roll_dice_default():
    d6 = roll_dice()

    assert d6 <= 6 and d6 >= 1
    
def test_roll_dice_one():
    d6 = roll_dice("4")

    assert d6 <= 4 and d6 >= 1
    
def test_roll_dice_two():
    d6 = roll_dice("2", "5")

    assert d6 <= 5 and d6 >= 2