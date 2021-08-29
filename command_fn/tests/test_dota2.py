from command_fn.dota2 import get_single_draft


def test_single_draft():
    draft = get_single_draft()
    print(draft)
    assert len(draft.split("\n")) == 4