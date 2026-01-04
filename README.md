# Plan
A small, testable command-line Tic-Tac-Toe in Python with a clean game loop, a simple board model, and isolated validation/win logic to keep tests straightforward.

# Installation
- `uv venv`
- `source .venv/bin/activate`
- `uv pip install -e '.[dev]'`

# Run
- `python3 -m tic_tac_toe`
- `python3 -m tic_tac_toe --human-vs-human`

# Tests
- `python3 -m pytest`
- `python3 -m pytest --cov=tic_tac_toe --cov-report=term-missing`

# Lint/Format
- `ruff check .` (lint)
- `ruff format --check .` (format)

# Example session
```
$ python3 -m tic_tac_toe --human-vs-human
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
X move (1-9): 1
X | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
O move (1-9): 2
X | O | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
X move (1-9): 4
X | O | 3
---------
X | 5 | 6
---------
7 | 8 | 9
O move (1-9): 5
X | O | 3
---------
X | O | 6
---------
7 | 8 | 9
X move (1-9): 7
X | O | 3
---------
X | O | 6
---------
X | 8 | 9
X wins
```

# Action items
[x] Sketch minimal module layout and define public functions/classes for board state and move application.

[x] Implement board representation and rendering for a 3x3 grid with 1–9 positions.

[x] Add move parsing/validation to reject invalid characters, out-of-range inputs, and occupied cells.

[x] Implement win/draw detection for rows, columns, diagonals, and full-board draw.

[x] Add player loop that alternates X/O and supports human vs bot or human vs human play (no bot vs bot). The bot should always play the optimal move (or one of them) in any board scenario.

[x] Write pytest unit tests for win conditions, draw detection, and invalid move handling.

[x] Add tests for bot move legality and mixed human/bot turn flow.

[x] Implement CLI entrypoint with human input handling and bot responses.

[x] Verify CLI behavior manually with a few sample games and document run/test commands.

# Progress
- 2026-01-03 Phase 1: Added board model, win/draw rules, and core move validation tests.
- 2026-01-03 Phase 2: Added optimal bot, game loop, and flow tests.
- 2026-01-03 Phase 3: Added CLI entrypoint, input parsing, and related tests.
- 2026-01-03 Phase 4: Documented run/test commands, added an example session, ran pytest, and exercised win/draw CLI runs.
