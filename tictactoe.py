def inp1():  # INPUT OF PLAYER ONE
    return int(input("Where would you like to place your X : "))


def inp2():  # INPUT OF PLAYER 2
    return int(input("Where would you like to place your O : "))


game = ""


def draw():  # TO CHECK IF GAME ENDED WITH A DRAW
    if " " not in game_board[1::]:
        return "The game has ended with a draw"


def checker():  # TO CHECK WHO THE GAME WAS WON BY
    for i, j, k in victory:
        if game_board[i] == "X" and game_board[j] == "X" and game_board[k] == "X":
            return "The game is over and Player1 wins"
        elif game_board[i] == "O" and game_board[j] == "O" and game_board[k] == "O":
            return "The game is over and Player2 wins"


def board():  # TO PRINT THE BOARD
    print(game_board[7], "|", game_board[8], "|", game_board[9])
    print("----------")
    print(game_board[4], "|", game_board[5], "|", game_board[6])
    print("----------")
    print(game_board[1], "|", game_board[2], "|", game_board[3])


victory = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# POSSIBLE CASES RESULTING IN VICTORY

game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # LIST FOR GAME BOARD

play = input("Do you want to play a game of TicTacToe? Yes or No : ")
while play == "Yes" or play == "yes":
    while game != "over":
        move1 = inp1()
        if game_board[move1] == " ":
            game_board[move1] = "X"
        else:
            print("Enter a valid a value")
            continue
        board()
        game = checker()
        if game == "The game is over and Player1 wins":
            print(game)
            break
        if draw() == "The game has ended with a draw":
            print(draw())
            break
        move2 = inp2()
        if game_board[move2] == " ":
            game_board[move2] = "O"
        else:
            print("Enter a valid a value")
            continue
        board()
        game = checker()
        if game == "The game is over and Player2 wins":
            print(game)
            break
        if draw() == "The game has ended with a draw":
            print(draw())
            break
    for i in range(10):
            game_board[i] = " "
    play = input("Do you want to play another game of TicTacToe? Yes or No : ")
