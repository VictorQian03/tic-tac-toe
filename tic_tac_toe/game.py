from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Optional

from .board import Board
from .rules import check_winner, is_draw

Player = Callable[[Board, str], int]


@dataclass(frozen=True)
class GameResult:
    winner: Optional[str]
    is_draw: bool
    final_board: Board
    moves: tuple[int, ...]


def play_game(
    x_player: Player, o_player: Player, board: Optional[Board] = None
) -> GameResult:
    current_board = board or Board()
    moves: list[int] = []
    players = {"X": x_player, "O": o_player}
    mark = "X"

    while True:
        winner = check_winner(current_board)
        if winner is not None:
            return _result(winner, False, current_board, moves)
        if is_draw(current_board):
            return _result(None, True, current_board, moves)

        move = players[mark](current_board, mark)
        current_board = current_board.apply_move(move, mark)
        moves.append(move)
        mark = "O" if mark == "X" else "X"


def _result(
    winner: Optional[str],
    is_draw_result: bool,
    final_board: Board,
    moves: list[int],
) -> GameResult:
    return GameResult(
        winner=winner,
        is_draw=is_draw_result,
        final_board=final_board,
        moves=tuple(moves),
    )
