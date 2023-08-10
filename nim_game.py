"""Nim is a game of strategy in which two players take turns removing sticks from distinct piles.
"""


def game():
    """The part where the general process of the game is controlled"""
    number_of_sticks = 11
    player1 = str(input("Please enter the name of the 1st player: "))
    player2 = str(input("Please enter the name of the 2nd player: "))
    turn = player1
    game_table(number_of_sticks)
    while True:
        print("\nPlayer: " + turn)
        player_action = game_sequence()
        if player_action:
            number_of_sticks = number_of_sticks - player_action
            if number_of_sticks <= 0:
                print()
                game_end(turn)
                break
            game_table(number_of_sticks)
            turn = player_rotation(player1, player2, turn)


def game_table(number_of_sticks):
    """Function to draw the game board

    Args:
        number_of_sticks (int): Number of sticks currently available on the board
    """
    print("\n" + "====== " * number_of_sticks)
    for i in range(1, (number_of_sticks + 1)):
        print("|", format(i, "02d"), "|", end=" ")
    print("\n" + "====== " * number_of_sticks)


def game_end(turn):
    """Function to declare the winner at the end of the game

    Args:
        turn (str): Value indicating who is the current turn
    """
    winner = "Game over. Player " + turn + " has won."
    length = len(winner) + 6
    print("=" * length, end="\n")
    print("|| " + winner + " ||")
    print("=" * length, end="\n")
    decision = input("\nDo you want to play one more time?:(Y/N) ")
    if decision.upper() == "Y":
        game()
    elif decision.upper() == "N":
        print("\nOkey good Bye T_T")

def game_sequence():
    """Function that receives the number of sticks from users for the game

    Returns:
        player_action(int): number of sticks to be removed/take
    """
    while True:
        player_action = input(
            "Please enter the number of sticks you would like to take: "
        )
        if player_action.upper() == "Q":
            return
        try:
            player_action = int(player_action)
        except ValueError:
            print("Please enter a number between 1 and 3 or press Q/q to exit")
        else:
            if 1 <= player_action <= 3:
                return player_action
            else:
                print("The selected number must be between 1 and 3. Press Q/q to exit")


def player_rotation(player1, player2, turn):
    """_summary_

    Args:
        player1 (str): First player's name
        player2 (str): Second player's name
        turn (str): Value indicating who is the current turn

    Returns:
        turn(str): current turn
    """
    if turn == player1:
        return player2
    else:
        return player1

if __name__ == "__main__":
    print(
        """In the Nim Game, there are initially 11 sticks on the table
Two players take turns to take away one, two or three sticks.
The person who takes the last stick/sticks wins. !!!\n"""
    )
    game()
