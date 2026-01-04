# Tic-Tac-Toe CLI Plan

## Goal
Implement or refactor the Python CLI tic-tac-toe game in this repo, including the board model, move validation, win/draw logic, game loop, and bot behavior.

## Required Files And Responsibilities
- Implement `tic_tac_toe/__init__.py` to expose the main public API (board, rules, bot, and CLI entrypoint).
- Implement `tic_tac_toe/board.py` with a small board model for a 3x3 grid using positions 1-9, including helpers to apply moves, list available moves, and render the board for CLI output.
- Implement `tic_tac_toe/rules.py` with pure win/draw detection for rows, columns, diagonals, and full-board draw; avoid side effects and I/O.
- Implement `tic_tac_toe/bot.py` with an optimal-move selector (minimax or equivalent) that always returns a legal move and uses a deterministic tie-breaker (lowest index) for tests.
- Implement `tic_tac_toe/game.py` to orchestrate turn order, alternate X/O, and return a clear result payload (winner or draw) without printing.
- Implement `tic_tac_toe/cli.py` to handle user input parsing, validation errors, board display, and to call the game loop with human/bot players.
- Implement `tic_tac_toe/__main__.py` to provide a `python -m tic_tac_toe` entrypoint that calls `cli.main()`.

## Interface And I/O Expectations
- `tic_tac_toe/board.py`
  - Board positions map 1-9, left-to-right, top-to-bottom (1-3 top row, 7-9 bottom row).
  - `Board` stores 9 cells using `"X"`, `"O"`, or `None` for empty.
  - `available_moves()` returns a sorted list of open positions (ints 1-9).
  - `apply_move(position, mark)` validates `position` and `mark` and returns an updated board (new instance or in-place, but consistent across the codebase); raise `ValueError` for out-of-range or occupied moves.
  - `render()` returns a string suitable for CLI output; empty cells should show their position number so players can see legal inputs.
- `tic_tac_toe/rules.py`
  - `check_winner(cells_or_board)` returns `"X"`, `"O"`, or `None`.
  - `is_draw(cells_or_board)` returns `True` only when the board is full and there is no winner.
  - Functions are pure: no printing, no mutation of inputs.
- `tic_tac_toe/bot.py`
  - `choose_move(board, mark)` (and optional `opponent_mark`) returns a legal move int from `available_moves()`.
  - Deterministic tie-breaker: when multiple moves are equally optimal, return the lowest position.
  - If called on a terminal board, either raise a clear error or return `None` (pick one and document).
- `tic_tac_toe/game.py`
  - `play_game(x_player, o_player, board=None)` runs a full game without I/O.
  - Player callables accept `(board, mark)` and return a move int.
  - Returns a result payload like `{"winner": "X"|"O"|None, "is_draw": bool, "final_board": Board, "moves": list[int]}` (exact shape can vary, but it must clearly communicate winner vs draw and the ending board).
- `tic_tac_toe/cli.py`
  - `main(argv=None)` runs a single game and returns an exit code (`0` on success).
  - Reads user input (digits 1-9); on invalid input or occupied move, prints a short error and re-prompts.
  - Prints the board before each human move and prints a final outcome message (`X wins`, `O wins`, or `Draw`).
- `tic_tac_toe/__init__.py` and `tic_tac_toe/__main__.py`
  - Export the primary API (`Board`, rules helpers, `choose_move`, `play_game`, `main`) from `__init__.py`.
  - `python -m tic_tac_toe` calls `cli.main()` directly.

## Implementation Sketches
- Win/Draw Detection
  - Normalize input into a 9-cell list.
  - Precompute winning line indices: rows, columns, diagonals.
  - If any line has the same non-`None` mark, return that mark as winner.
  - Draw is `board full && no winner`.
- Minimax Bot (Deterministic)
  - Base case: if winner/draw, return score (`+1` win, `0` draw, `-1` loss) with no move.
  - For each available move: apply move, recurse for opponent, invert score.
  - Select the move with the highest score; if tie, choose the lowest position.
- Game Loop
  - Start with an empty board; current mark `"X"`.
  - While no winner and not draw: call the current player to get a move, apply it, switch mark.
  - Return the final board and outcome in a structured result.
- CLI Loop
  - Decide player types based on args: default to human vs bot (human as X, bot as O), allow `--bot-first`, and add `--human-vs-human` for two humans (no bot vs bot).
  - For human turns: render board, prompt input, validate, and re-prompt on error.
  - For bot turns: call `choose_move` and display the chosen move before rendering updated board.

## Documentation Requirements
- Update `README.md` with run and test commands, plus a short example of a CLI game session.
- Add short module docstrings only where the purpose is not obvious from the module name.
