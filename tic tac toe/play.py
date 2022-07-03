import random
import player
import game

letters = ['X','O']
random.shuffle(letters)
print(letters)
print("player 1 will be", letters[0], " and player 2 will be", letters[1])

player_one = input("Would you like player 1 to be a human or robot? H for human, R for robot.").upper()
while player_one != 'H' and player_one != 'R':
    print("Invalid input. Try again\n")
    player_one = input("Would you like player 1 to be a human or robot? H for human, R for Robot.").upper()

if player_one == 'H':
    game_one = player.HumanPlayer(letters[0])
else:
    game_one = player.ComputerPlayer(letters[0])

player_two = input("Would you like player 2 to be a human or robot? H for human, R for robot.").upper()
while player_two != 'H' and player_two != 'R':
    print("Invalid input. Try again\n")
    player_two = input("Would you like player 2 to be a human or robot? H for human, R for robot.").upper()

if player_two == 'H':
    game_two = player.HumanPlayer(letters[1])
else:
    game_two = player.ComputerPlayer(letters[1])

def play(game, player_one, player_two):
    player_turn = letters[0]
    while game.game_over() == False:
        game.print_board()
        game.print_available_moves()
        if player_turn == letters[0]:
            move = player_one.get_move(game)
            game.make_move(move,player_turn)
        else:
            move = player_two.get_move(game)
            game.make_move(move,player_turn)
        if player_turn == letters[0]:
            player_turn = letters[1]
        else:
            player_turn = letters[0]
    game.print_board()
    if player_turn == letters[0]:
            player_turn = letters[1]
    else:
        player_turn = letters[0]       
    if game.winner() == True:
        print("The game is over, player", (letters.index(player_turn) + 1), "also known as player", player_turn, "has won!")
    else:
        print("The game is over. It is a draw.")                  

play(game.TicTacToe(),game_one,game_two)