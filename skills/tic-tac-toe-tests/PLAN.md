# Tic-Tac-Toe Tests Plan

## Goal
Create or update pytest coverage for the tic-tac-toe project, including win/draw detection, move validation, bot legality/optimality, and mixed human/bot turn flow.

## Required Test Files And Responsibilities
- Implement `tests/test_rules.py` to cover row, column, diagonal wins, and draw detection using explicit board states.
- Implement `tests/test_moves.py` to cover invalid input parsing (non-digit, out of range), and occupied-cell rejection.
- Implement `tests/test_bot.py` to verify the bot always returns a legal move and chooses a winning or blocking move when available.
- Implement `tests/test_game_flow.py` to cover alternating turns, mixed human/bot play, and game termination on win or draw.

## Coverage Notes
- Use `pytest` with deterministic board setups; avoid randomness unless seeded and asserted.
- Keep tests I/O-free by injecting move selectors or input functions instead of reading from stdin.
- Use the same 1-9 position mapping as the CLI to prevent mismatch between UI and rules.
- Add a small CLI argument test to confirm `--human-vs-human` and `--bot-first` select the expected player types.
