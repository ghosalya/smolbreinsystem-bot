from command_fn import pbem


class MockChannel:
    def __init__(self, id):
        self.id = id

    def send(self, msg):
        print(msg)


def test_get_player_name():
    assert pbem.get_player_name("player1") == "@player1"
    assert pbem.get_player_name("@player2") == "@player2"


def test_next_turn_zero():
    assert pbem.next_turn(channel=MockChannel(1)) == "Please provide player name (e.g. `$nextturn @player`)"


def test_next_turn_one():
    player_name = "player"
    assert pbem.next_turn(player_name, channel=MockChannel(1)) == "Reminder set for @player!"
    assert pbem.SESSIONS[1]["DEFAULT"]["message"] == "@player"


def test_next_turn_two():
    player_name = "player2"

    assert pbem.next_turn(player_name, "session", channel=MockChannel(1)) == "Game session name must start with `#` (e.g. `$nextturn @player #game`)"

    assert pbem.next_turn(player_name, "#session", channel=MockChannel(1)) == "Reminder set for @player2 (for session #session)!"
    assert pbem.SESSIONS[1]["#session"]["message"] == "@player2"
    

def test_clear_turn_zero():
    player_name = "player"
    pbem.next_turn(player_name, channel=MockChannel(1))
    assert pbem.SESSIONS[1]["DEFAULT"]["message"] == "@player"

    assert pbem.clear_turn(channel=MockChannel(1)) == "NextTurn: default session cleared."
    assert pbem.SESSIONS[1]["DEFAULT"] is None


def test_clear_turn_one():
    player_name = "player2"
    session_name = "#session"
    pbem.next_turn(player_name, session_name, channel=MockChannel(1))
    assert pbem.SESSIONS[1][session_name]["message"] == "@player2"

    assert pbem.clear_turn(session_name, channel=MockChannel(1)) == "NextTurn: session #session cleared."
    assert pbem.SESSIONS[1][session_name] is None