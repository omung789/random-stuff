import random

#abstract player class
class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

#computer player class that uses randomised numbers to select moves - needs proper ai
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    #num = random.choice(game.available_moves() another more elegant solution)
    #makes random move
    def get_move(self, game):
        num = random.randint(0,8)
        while num not in game.available_moves():
            num = random.randint(0,8)
        return num

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    # obtains move that user requests
    def get_move(self, game):
        valid_num = False
        num = None
        while not valid_num:
            num = (input(self.letter + "'s turn. give a number thats free on the board."))
            try:
                num = int(num)
                if num not in game.available_moves():
                    raise ValueError
                valid_num = True    
            except ValueError:
                print("invalid input, try again.")        
        return num