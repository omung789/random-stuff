class TicTacToe:
    def __init__(self):
        self.board = [[' ' for x in range(3)] for y in range(3)]

    def print_board(self):
        for i in range(3):    
            print(self.board[i])
        print("\n")    

    def print_available_moves(self):
        moves = self.available_moves()
        print_moves = [[' ' for x in range(3)] for y in range(3)]
        for y in range(3):
            for x in range(3):
                if y + x*3 in moves:
                    print_moves[x][y] = y + x*3
                else:
                    print_moves[x][y] = ' '    
        print("available moves are:")
        for i in print_moves:
            print(i)
        print("\n")                


    def available_moves(self):
        moves = []
        for y in range(3):
            for x in range(3):
                if self.board[x][y] == ' ':
                    moves.append(y + x*3)
        return moves

    def make_move(self,move,letter):
        available = self.available_moves()
        y = move % 3
        x = move // 3
        if move in available:
            self.board[x][y] = letter
            self.game_over()

    def game_over(self):
        #check horizontally and vertically
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return True
        #check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[2][0] != ' ':
            return True
        #if no winner and board is full, game ended in a draw
        if len(self.available_moves()) == 0:
            #print("draw")
            return True
        return False

    def winner(self):
        #check horizontally and vertically
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return True
        #check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]and self.board[0][0] != ' ':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[2][0] != ' ':
            return True
        return False            
            
#   0 1 2
# 0 0 1 2
# 1 3 4 5 
# 2 6 7 8


# ttt = TicTacToe()
# ttt.print_board()
# print(ttt.available_moves())
# ttt.make_move(4,'X')
# ttt.print_board()