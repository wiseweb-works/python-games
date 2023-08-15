"""Connect Four (also known as Connect 4) is a two-player connection rack game,
in which the players choose a color and then take turns dropping colored tokens
into a six-row, seven-column vertically suspended grid"""


def game():
    """The part where the general process of the game is controlled"""
    turn = X
    table = ["[ ]"] * 43
    game_table(table)
    while True:
        game_sequence(turn, table)
        game_table(table)
        if win_check(table) is True:
            game_table(table)
            print(f"""\n###############\n# Winner:  {turn}  #\n###############""")
            break
        elif win_check(table) == "T":
            print(
                """\n#################\n#  Game is Over #
#\033[1;33m It's so Rare \033[0m #\n# But sadly Tie #\n#################"""
            )
            break
        else:
            turn = player_rotation(turn)


def game_table(table):
    """Function to draw the game board

    Args:
        table (list): list of moves made during the game"""
    for i in range(1, 43, 7):
        print(*table[i : i + 7], sep=" ")
    print("""--- --- --- --- --- --- ---\n[1] [2] [3] [4] [5] [6] [7]\n""")


def game_sequence(turn, table):
    """Function that receives the decisions from users for the game

    Args:
        turn (str): Value indicating who is the current turn
        table (list): list of moves made during the game"""
    hamle = int(input(f"Player {turn} Please type your move (1-7): "))
    print()
    if table[hamle] == "[ ]":
        for i in range(35, -1, -7):
            if table[hamle + i] == "[ ]":
                table[hamle + i] = f"[{turn}]"
                return player_rotation(turn)
    else:
        print("You have selected the filled place. Please try again.")
        game_sequence(turn, table)


def win_check(table):
    """Function to check the winner during the game

    Args:
        table (list): list of moves made during the game

    Returns:
        True or T: Returns win or draw status"""

    # Horizontal Control
    for i in range(1, 37, 7):
        for _ii in range(0, 4):
            if (
                table[i + _ii]
                == table[i + _ii + 1]
                == table[i + _ii + 2]
                == table[i + _ii + 3]
            ):
                if table[i + 3] == "[" + X + "]":
                    table[i + _ii] = table[i + _ii + 1] = table[i + _ii + 2] = table[
                        i + _ii + 3
                    ] = "\033[0;34m[=]\033[0m"
                    return True
                elif table[i + 3] == "[" + O + "]":
                    table[i + _ii] = table[i + _ii + 1] = table[i + _ii + 2] = table[
                        i + _ii + 3
                    ] = "\033[0;31m[=]\033[0m"
                    return True

    # Vertical Control
    for i in range(0, 15, 7):
        for _ii in range(1, 8):
            if (
                table[i + _ii]
                == table[i + _ii + 7]
                == table[i + _ii + 14]
                == table[i + _ii + 21]
            ):
                if table[i + _ii + 21] == "[" + X + "]":
                    table[i + _ii] = table[i + _ii + 7] = table[i + _ii + 14] = table[
                        i + _ii + 21
                    ] = "\033[0;34m[|]\033[0m"
                    return True
                elif table[i + _ii + 21] == "[" + O + "]":
                    table[i + _ii] = table[i + _ii + 7] = table[i + _ii + 14] = table[
                        i + _ii + 21
                    ] = "\033[0;31m[|]\033[0m"
                    return True

    # Cross Check
    for i in range(0, 15, 7):
        for _ii in range(1, 5):
            if (
                table[i + _ii]
                == table[i + _ii + 8]
                == table[i + _ii + 16]
                == table[i + _ii + 24]
            ):
                if table[i + _ii + 16] == "[" + X + "]":
                    table[i + _ii] = table[i + _ii + 8] = table[i + _ii + 16] = table[
                        i + _ii + 24
                    ] = "\033[0;34m[" + chr(92) + "]\033[0m"
                    return True
                elif table[i + _ii + 16] == "[" + O + "]":
                    table[i + _ii] = table[i + _ii + 8] = table[i + _ii + 16] = table[
                        i + _ii + 24
                    ] = "\033[0;31m[" + chr(92) + "]\033[0m"
                    return True

    # Cross Check 2
    for i in range(0, 15, 7):
        for _ii in range(4, 8):
            if (
                table[i + _ii]
                == table[i + _ii + 6]
                == table[i + _ii + 12]
                == table[i + _ii + 18]
            ):
                if table[i + _ii + 12] == "[" + X + "]":
                    table[i + _ii] = table[i + _ii + 6] = table[i + _ii + 12] = table[
                        i + _ii + 18
                    ] = "\033[0;34m[/]\033[0m"
                    return True
                elif table[i + _ii + 12] == "[" + O + "]":
                    table[i + _ii] = table[i + _ii + 6] = table[i + _ii + 12] = table[
                        i + _ii + 18
                    ] = "\033[0;31m[/]\033[0m"
                    return True

    # Tie Probability Check
    if table.count("[" + X + "]") + table.count("[" + O + "]") == 42:
        return "T"


def player_rotation(turn):
    """Function to change the player turn

    Args:
        turn (str): Value indicating who is the current turn

    Returns:
        turn(str): current turn"""
    if turn == X:
        return O
    else:
        return X


if __name__ == "__main__":
    print(
        """Players drop blue or red discs into the grid, starting in the middle or at the edge
to stack their colored discs (\033[1;33m↑, ↓, ⇄, or ⤭\033[0m). Use strategy to block opponents
while aiming to be the first player to get 4 in a row to win."""
    )
    X = "\033[0;34mX\033[0m"
    O = "\033[0;31mO\033[0m"
    game()
    