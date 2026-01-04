from tic_tac_toe.board import Board
from tic_tac_toe.bot import choose_move


def test_choose_move_returns_legal_move() -> None:
    board = Board(["X", None, "O", None, "X", None, None, "O", None])
    move = choose_move(board, "X")
    assert move in board.available_moves()


def test_choose_move_finds_winning_move() -> None:
    board = Board(["X", "X", None, "O", "O", None, None, None, None])
    assert choose_move(board, "X") == 3


def test_choose_move_blocks_opponent() -> None:
    board = Board(["X", "X", None, None, "O", None, None, None, None])
    assert choose_move(board, "O") == 3


def test_choose_move_tiebreaks_lowest_index() -> None:
    board = Board(["X", "X", None, "O", "X", None, "O", None, None])
    assert choose_move(board, "X") == 3
