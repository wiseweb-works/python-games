"""Tic-tac-toe is an instance of an m,n,k-game, 
where two players alternate taking turns on an m×n board until one of them gets k in a row"""


def game():
    """The part where the general process of the game is controlled"""
    turn = X
    table = [*range(0, 10, 1)]
    game_table(table)
    while True:
        game_sequence(turn, table)
        game_table(table)
        if win_check(table) is True:
            print(f"""\n###############\n# Winner:  {turn}  #\n###############""")
            break
        elif win_check(table) == "T":
            print(
                """\n#############\n# Game Over #\n# \033[1;33mSadly Tie\033[0m #\n#############"""
            )
            break
        turn = player_rotation(turn)


def game_table(table):
    """Function to draw the game board

    Args:
        table (list): list of moves made during the game"""
    print(
        f"""+-------------------+
|                   |
|  [{table[7]}] | [{table[8]}] | [{table[9]}]  |
|  ----+-----+----  |
|  [{table[4]}] | [{table[5]}] | [{table[6]}]  |
|  ----+-----+----  |
|  [{table[1]}] | [{table[2]}] | [{table[3]}]  |
|                   |
+-------------------+"""
    )


def game_sequence(turn, table):
    """Function that receives the decisions from users for the game

    Args:
        turn (str): Value indicating who is the current turn
        table (list): list of moves made during the game"""
    player_action = int(input("Player " + turn + " Please type your move (1-9): "))
    print()
    if table[player_action] != X and table[player_action] != O:
        table[player_action] = turn

    else:
        print("You have selected the filled place. Please try again.")
        game_sequence(turn, table)


def win_check(table):
    """Function to check the winner during the game

    Args:
        table (list): list of moves made during the game

    Returns:
        True or T: Returns win or draw status"""
    for i in range(1, 8, 3):
        if table[i] == table[i + 1] == table[i + 2]:
            return True

    for i in range(1, 4):
        if table[i] == table[i + 3] == table[i + 6]:
            return True

    if table[1] == table[5] == table[9] or table[3] == table[5] == table[7]:
        return True

    if table.count(X) + table.count(O) == 9:
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
        """The game is played on a grid that's 3 squares by 3 squares.
You are X , your friend is O. Players take turns putting their marks in empty squares.
The first player to get 3 of her marks in a row (\033[1;33m↑, ↓, ⇄, or ⤭\033[0m) is the winner.\n"""
    )
    X = "\033[0;34mX\033[0m"
    O = "\033[0;31mO\033[0m"
    game()
