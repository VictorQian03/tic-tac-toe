from tic_tac_toe.board import Board
from tic_tac_toe.rules import check_winner, is_draw


def test_row_win() -> None:
    board = Board(["X", "X", "X", None, "O", None, None, "O", None])
    assert check_winner(board) == "X"


def test_column_win() -> None:
    board = Board(["O", None, "X", "O", "X", None, "O", None, "X"])
    assert check_winner(board) == "O"


def test_diagonal_win() -> None:
    board = Board(["X", "O", None, None, "X", None, None, "O", "X"])
    assert check_winner(board) == "X"


def test_draw_detection() -> None:
    board = Board(["X", "O", "X", "X", "O", "O", "O", "X", "X"])
    assert check_winner(board) is None
    assert is_draw(board) is True
