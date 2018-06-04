import random

board = [" " for i in range(9)]
icon = "X"


# display the game board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


# move functions
def player_move(icon):
    print("Your turn player {}!".format(icon))

    while True:
        choice = int(input("Enter your move(1-9): ").strip())
        if is_available(choice):
            board[choice - 1] = icon
            break
        else:
            print("Sorry, that space has already been taken. Try again...")


def computer_move(icon):
    while True:
        choice = random.randint(1, 9)
        if is_available(choice):
            board[choice - 1] = icon
            print("Computers choice is {}".format(choice))
            break


# Checks to see if the game has been won
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        print_board()
        print("{} wins the game! Congratulations!".format(icon))
        return True
    else:
        return False


# Checks to see if there are no more possible spaces
def is_draw():
    if " " not in board:
        print_board()
        print("Dang! It's a Draw... Game Over")
        return True
    else:
        return False


# Checks to see if the chosen space is available
def is_available(choice):
    if board[choice - 1] != " ":
        return False
    else:
        return True


# Settle on the number of players that will play the game
while True:
    players = int(input(
        "How many players will be playing? (1 or 2): "
    ).strip())
    if players > 2:
        print("That's too many players! Try again...")
    elif players < 1:
        print("That's not enough players! Try again...")
    else:
        if players == 1:
            print(
                "Great! Player 1, you'll be X!"
            )
            comp = True
        if players == 2:
            print(
                "Great! Player 1 will be X and Player 2 will be O!"
            )
            comp = False
        print("Let's get started...")
        break

while True:
    print_board()
    if icon == "X":
        player_move(icon)
        if is_victory(icon):
            break
        if is_draw():
            break
        icon = "O"
    elif players == 2 and icon == "O":
        player_move(icon)
        if is_victory(icon):
            break
        if is_draw():
            break
        icon = "X"
    else:
        computer_move(icon)
        if is_victory(icon):
            break
        if is_draw():
            break
        icon = "X"
