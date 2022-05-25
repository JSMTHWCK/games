from player import *

class Game:

    def __init__(self,p_one, p_two):
        self.players = [p_one,p_two]
        self.turn = 0
        self.board = [[0 for i in range(7)] for i in range(6)]

    def print_board(self):
        for i in self.board:
            print(i)
        print('')
    
    def nest_copy(self):
        new_list = []
        for i in self.board:
            new_list.append(i)
        return new_list

    def make_move(self):
        self.turn = self.turn %2 + 1
        plr = self.players[self.turn - 1]
        plr_mv = plr.choose_move(self.nest_copy())
        for i in range(5,-1,-1):
            if self.board[i][plr_mv] == 0:
                self.board[i][plr_mv] = self.turn
                break

                
    def is_end(self,board):
        #horizontal
        for i in range(0,6):
            for j in range(0,4):
                last_piece = board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                    return str(last_piece)
        #vertical
        for i in range(0,3):
            for j in range(0,7):
                last_piece = board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                    return str(last_piece)
        #diagonal (\)
        for i in range(0,3):
            for j in range(0,4):
                last_piece = board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                    return str(last_piece)
        #diagonal (/)
        for i in range(5,2,-1):
            for j in range(0,4):
                last_piece == board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
                    return str(last_piece)
        for i in board:
            if 0 in i:
                return False
        return 'Tie'

    def game(self,log = False):
        while True:
            if log == True:
                self.print_board()
            if self.is_end(list(self.board)) != False:
                return self.is_end(list(self.board))
            self.make_move()
        
            
