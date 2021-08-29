import bot


def test_all_commands():
    for name, fn in bot.COMMANDS.items():
        assert fn() is not None, "Function for " + name + " did not return!"
