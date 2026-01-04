import pytest

from tic_tac_toe.board import Board
from tic_tac_toe.cli import parse_move


@pytest.mark.parametrize("position", [0, 10])
def test_apply_move_out_of_range(position: int) -> None:
    board = Board()
    with pytest.raises(ValueError):
        board.apply_move(position, "X")


@pytest.mark.parametrize("position", ["a", "3"])
def test_apply_move_non_digit(position: str) -> None:
    board = Board()
    with pytest.raises(ValueError):
        board.apply_move(position, "X")


def test_apply_move_occupied_cell() -> None:
    board = Board().apply_move(5, "X")
    with pytest.raises(ValueError):
        board.apply_move(5, "O")


def test_apply_move_invalid_mark() -> None:
    board = Board()
    with pytest.raises(ValueError):
        board.apply_move(4, "Z")


@pytest.mark.parametrize("text, expected", [("1", 1), (" 5 ", 5), ("9", 9)])
def test_parse_move_accepts_digits(text: str, expected: int) -> None:
    assert parse_move(text) == expected


@pytest.mark.parametrize("text", ["", "a", "5a", "10", "0", "03"])
def test_parse_move_rejects_invalid_text(text: str) -> None:
    with pytest.raises(ValueError):
        parse_move(text)
