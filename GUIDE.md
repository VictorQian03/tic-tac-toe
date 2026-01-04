# Implementation Guide (Phased)

This guide is the entrypoint for Codex. For each phase, read the reference docs in
`skills/tic-tac-toe-cli/` and the test docs in `skills/tic-tac-toe-tests/`. The
reference and test tracks must move together: implement code and tests in the same
phase, then verify.

Workflow rules for every phase:
- Read the relevant `SKILL.md`, `PLAN.md`, and `VERIFY.md` files before changing code.
- Implement the plan items for that phase and follow the interface specs.
- Add or update tests that cover the phase changes.
- Run the verification steps for the phase.
- Update progress in `README.md` so humans can track what is done and re-run checks.

## Phase 1: Board model + rules + core tests

Read:
- `skills/tic-tac-toe-cli/SKILL.md`
- `skills/tic-tac-toe-cli/PLAN.md`
- `skills/tic-tac-toe-cli/VERIFY.md`
- `skills/tic-tac-toe-tests/SKILL.md`
- `skills/tic-tac-toe-tests/PLAN.md`
- `skills/tic-tac-toe-tests/VERIFY.md`

Implement:
- `tic_tac_toe/board.py` with 1-9 position mapping, move validation, and render output.
- `tic_tac_toe/rules.py` with pure win/draw detection.

Tests:
- `tests/test_rules.py` for row/column/diagonal wins and draws.
- `tests/test_moves.py` for invalid inputs and occupied-cell rejection.

Verify:
- Run `pytest` (or the tests that exist so far).
- Manually reason through board rendering to ensure positions 1-9 display.

README.md update:
- Check off action items for board representation, win/draw detection, and invalid move handling.
- Add a short "Progress" note for Phase 1 (date + one-line summary).

## Phase 2: Bot + game loop + flow tests

Read:
- `skills/tic-tac-toe-cli/SKILL.md`
- `skills/tic-tac-toe-cli/PLAN.md`
- `skills/tic-tac-toe-cli/VERIFY.md`
- `skills/tic-tac-toe-tests/SKILL.md`
- `skills/tic-tac-toe-tests/PLAN.md`
- `skills/tic-tac-toe-tests/VERIFY.md`

Implement:
- `tic_tac_toe/bot.py` with deterministic optimal move selection.
- `tic_tac_toe/game.py` with a pure game loop and result payload.

Tests:
- `tests/test_bot.py` for legal moves and win/block behavior.
- `tests/test_game_flow.py` for alternating turns and termination on win/draw.

Verify:
- Run `pytest`.
- Confirm bot tie-breakers are deterministic (lowest index).

README.md update:
- Check off action items for bot and turn loop.
- Add a short "Progress" note for Phase 2.

## Phase 3: CLI + entrypoints + input handling

Read:
- `skills/tic-tac-toe-cli/SKILL.md`
- `skills/tic-tac-toe-cli/PLAN.md`
- `skills/tic-tac-toe-cli/VERIFY.md`
- `skills/tic-tac-toe-tests/SKILL.md`
- `skills/tic-tac-toe-tests/PLAN.md`
- `skills/tic-tac-toe-tests/VERIFY.md`

Implement:
- `tic_tac_toe/cli.py` for user prompts, validation, output, and a `--human-vs-human` option (keep human vs bot as the default).
- `tic_tac_toe/__init__.py` and `tic_tac_toe/__main__.py` for public API and `python -m`.

Tests:
- Extend `tests/test_moves.py` for input parsing behavior without stdin.
- Add or adjust `tests/test_game_flow.py` if CLI logic impacts turn flow.

Verify:
- Run `pytest`.
- Manual check: run `python3 -m tic_tac_toe` and play a short game.
- Manual check: run `python3 -m tic_tac_toe --human-vs-human` and play a short game.
- Confirm invalid inputs are rejected and the board updates each turn.

README.md update:
- Check off action items for CLI behavior and mixed human/bot flow.
- Add a short "Progress" note for Phase 3.

## Phase 4: Docs + final verification

Read:
- `skills/tic-tac-toe-cli/PLAN.md`
- `skills/tic-tac-toe-cli/VERIFY.md`
- `skills/tic-tac-toe-tests/VERIFY.md`

Implement:
- Update `README.md` with run/test commands and a short example session.
- Ensure all modules match the plan and exposed API is complete.

Verify:
- Run full `pytest`.
- Manual check: play a win and a draw scenario from the CLI.

README.md update:
- Check off remaining action items.
- Add a final "Progress" note for Phase 4 with verification steps.
