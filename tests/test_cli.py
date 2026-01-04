import pytest

from tic_tac_toe.cli import resolve_player_kinds


def test_resolve_player_kinds_defaults_to_human_vs_bot() -> None:
    assert resolve_player_kinds([]) == ("human", "bot")


def test_resolve_player_kinds_bot_first() -> None:
    assert resolve_player_kinds(["--bot-first"]) == ("bot", "human")


def test_resolve_player_kinds_two_humans() -> None:
    assert resolve_player_kinds(["--human-vs-human"]) == ("human", "human")


def test_resolve_player_kinds_rejects_conflicting_flags() -> None:
    with pytest.raises(ValueError):
        resolve_player_kinds(["--bot-first", "--human-vs-human"])
