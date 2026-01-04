from tic_tac_toe.game import play_game


def test_game_alternates_turns_and_stops_on_win() -> None:
    marks: list[str] = []
    x_moves = [1, 2, 3]
    o_moves = [4, 5]

    def x_player(board, mark):
        marks.append(mark)
        return x_moves.pop(0)

    def o_player(board, mark):
        marks.append(mark)
        return o_moves.pop(0)

    result = play_game(x_player, o_player)

    assert marks == ["X", "O", "X", "O", "X"]
    assert result.winner == "X"
    assert result.is_draw is False
    assert result.moves == (1, 4, 2, 5, 3)
    assert list(result.final_board.cells) == [
        "X",
        "X",
        "X",
        "O",
        "O",
        None,
        None,
        None,
        None,
    ]


def test_game_ends_on_draw() -> None:
    x_moves = [1, 3, 6, 8, 7]
    o_moves = [2, 5, 4, 9]

    def x_player(board, mark):
        return x_moves.pop(0)

    def o_player(board, mark):
        return o_moves.pop(0)

    result = play_game(x_player, o_player)

    assert result.winner is None
    assert result.is_draw is True
    assert result.moves == (1, 2, 3, 5, 6, 4, 8, 9, 7)
    assert list(result.final_board.cells) == [
        "X",
        "O",
        "X",
        "O",
        "O",
        "X",
        "X",
        "X",
        "O",
    ]
