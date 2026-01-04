from __future__ import annotations

from typing import Iterable, Optional, Sequence

VALID_MARKS = ("X", "O")


class Board:
    def __init__(self, cells: Iterable[Optional[str]] | None = None) -> None:
        if cells is None:
            cells_list: list[Optional[str]] = [None] * 9
        else:
            cells_list = list(cells)
            if len(cells_list) != 9:
                raise ValueError("Board requires exactly 9 cells.")
            for cell in cells_list:
                if cell is not None and cell not in VALID_MARKS:
                    raise ValueError("Cells must be 'X', 'O', or None.")

        self._cells: tuple[Optional[str], ...] = tuple(cells_list)

    @property
    def cells(self) -> Sequence[Optional[str]]:
        return self._cells

    def available_moves(self) -> list[int]:
        return [idx + 1 for idx, cell in enumerate(self._cells) if cell is None]

    def apply_move(self, position: int, mark: str) -> "Board":
        position = self._validate_position(position)
        self._validate_mark(mark)
        index = position - 1
        if self._cells[index] is not None:
            raise ValueError(f"Position {position} is already occupied.")

        updated = list(self._cells)
        updated[index] = mark
        return Board(updated)

    def render(self) -> str:
        def cell_text(index: int) -> str:
            value = self._cells[index]
            return value if value is not None else str(index + 1)

        rows = []
        for start in (0, 3, 6):
            row = " | ".join(cell_text(i) for i in range(start, start + 3))
            rows.append(row)
        return "\n---------\n".join(rows)

    @staticmethod
    def _validate_position(position: int) -> int:
        if isinstance(position, bool) or not isinstance(position, int):
            raise ValueError("Position must be an integer 1-9.")
        if position < 1 or position > 9:
            raise ValueError("Position must be between 1 and 9.")
        return position

    @staticmethod
    def _validate_mark(mark: str) -> None:
        if mark not in VALID_MARKS:
            raise ValueError("Mark must be 'X' or 'O'.")
