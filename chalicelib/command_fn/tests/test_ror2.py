from command_fn.ror2 import (
    get_ror2_build,
    get_ror2_char,
    get_ror2_equip
)


def test_build_noargs():
    # no args
    build1 = get_ror2_build()
    assert build1 is not None

def test_build_w_args():
    # with character
    build2 = get_ror2_build("commando")
    assert build2 is not None

def test_char():
    char = get_ror2_char()
    assert char is not None

def test_equip():
    equip = get_ror2_equip()
    assert "Equipment:" in equip

    # with FC count
    blast_shower = get_ror2_equip("Blast", "Shower")
    assert blast_shower == (
        "Equipment: Blast Shower\n"
        "Fuel cell breakpoints: 7, 10, 15"
    )

    # with acronym
    blast_shower = get_ror2_equip("sml")
    assert blast_shower == (
        "Equipment: Super Massive Leech\n"
        "Fuel cells for permanent uptime: 9"
    )