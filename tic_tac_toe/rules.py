from __future__ import annotations

from typing import Iterable, Optional

WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def check_winner(cells_or_board: Iterable[Optional[str]]) -> Optional[str]:
    cells = _coerce_cells(cells_or_board)
    for a, b, c in WINNING_LINES:
        mark = cells[a]
        if mark is not None and mark == cells[b] and mark == cells[c]:
            return mark
    return None


def is_draw(cells_or_board: Iterable[Optional[str]]) -> bool:
    cells = _coerce_cells(cells_or_board)
    return check_winner(cells) is None and all(cell is not None for cell in cells)


def _coerce_cells(cells_or_board: Iterable[Optional[str]]) -> list[Optional[str]]:
    if hasattr(cells_or_board, "cells"):
        cells = getattr(cells_or_board, "cells")
    else:
        cells = cells_or_board

    cells_list = list(cells)
    if len(cells_list) != 9:
        raise ValueError("Board requires exactly 9 cells.")
    return cells_list
