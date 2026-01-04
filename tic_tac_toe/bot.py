from __future__ import annotations

from typing import Optional

from .board import Board
from .rules import check_winner, is_draw

VALID_MARKS = ("X", "O")


def choose_move(board: Board, mark: str) -> int:
    """Return the optimal move for mark using a deterministic tie-breaker."""
    _validate_mark(mark)
    opponent = "O" if mark == "X" else "X"

    if check_winner(board) is not None or is_draw(board):
        raise ValueError("No moves available on a terminal board.")

    best_score = -2
    best_move: Optional[int] = None
    for move in board.available_moves():
        score = -_negamax(board.apply_move(move, mark), opponent)
        if score > best_score:
            best_score = score
            best_move = move

    if best_move is None:
        raise ValueError("No moves available on a terminal board.")
    return best_move


def _negamax(board: Board, mark: str) -> int:
    winner = check_winner(board)
    if winner is not None:
        return 1 if winner == mark else -1
    if is_draw(board):
        return 0

    opponent = "O" if mark == "X" else "X"
    best_score = -2
    for move in board.available_moves():
        score = -_negamax(board.apply_move(move, mark), opponent)
        if score > best_score:
            best_score = score
    return best_score


def _validate_mark(mark: str) -> None:
    if mark not in VALID_MARKS:
        raise ValueError("Mark must be 'X' or 'O'.")
