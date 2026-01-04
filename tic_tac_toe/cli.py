from __future__ import annotations

from collections.abc import Callable, Iterable
import sys

from .board import Board
from .bot import choose_move
from .game import Player, play_game

InputFunc = Callable[[str], str]
OutputFunc = Callable[[str], None]
PlayerKind = str


def parse_move(text: str) -> int:
    cleaned = text.strip()
    if len(cleaned) != 1 or cleaned not in "123456789":
        raise ValueError("Enter a number 1-9.")
    return int(cleaned)


def make_human_player(
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
) -> Player:
    def player(board: Board, mark: str) -> int:
        while True:
            output_func(board.render())
            response = input_func(f"{mark} move (1-9): ")
            try:
                move = parse_move(response)
                board.apply_move(move, mark)
                return move
            except ValueError as exc:
                output_func(str(exc))

    return player


def make_bot_player(output_func: OutputFunc = print) -> Player:
    def player(board: Board, mark: str) -> int:
        move = choose_move(board, mark)
        output_func(f"Bot chooses {move}.")
        return move

    return player


def _has_flag(argv: Iterable[str], flag: str) -> bool:
    return any(arg == flag for arg in argv)


def resolve_player_kinds(argv: Iterable[str]) -> tuple[PlayerKind, PlayerKind]:
    args = list(argv)
    bot_first = _has_flag(args, "--bot-first")
    human_vs_human = _has_flag(args, "--human-vs-human")
    if bot_first and human_vs_human:
        raise ValueError("Choose either --bot-first or --human-vs-human.")
    if human_vs_human:
        return ("human", "human")
    if bot_first:
        return ("bot", "human")
    return ("human", "bot")


def main(argv: Iterable[str] | None = None) -> int:
    args = list(argv) if argv is not None else list(sys.argv[1:])
    try:
        x_kind, o_kind = resolve_player_kinds(args)
    except ValueError as exc:
        print(str(exc))
        return 2

    human_player = make_human_player()
    bot_player = make_bot_player()
    players = {"human": human_player, "bot": bot_player}
    x_player = players[x_kind]
    o_player = players[o_kind]

    result = play_game(x_player, o_player)
    print(result["final_board"].render())
    if result["is_draw"]:
        print("Draw")
    else:
        print(f"{result['winner']} wins")
    return 0
