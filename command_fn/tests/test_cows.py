from command_fn.cows import get_advice, get_cow_games


def test_advice():
    advice = get_advice()
    assert advice is not None


def test_cowgames():
    game = get_cow_games()
    assert game is not None