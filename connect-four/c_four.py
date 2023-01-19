from player import *
"""
certain parts are seperated for easy access in c_four_tree.py
efficiency is not key here

"""
class Game:

    def __init__(self,player_one, player_two):
        self.players = [player_one,player_two]
        self.turn = 0
        self.board = [[0 for i in range(7)] for i in range(6)]

    def print_board(self):
        for row in self.board:
            print(row)
        print('')
    
    def copy_nest(self,board):
        new_list = []
        for row in board:
            new_list.append(list(row))
        return new_list

    def update_board(self,board,col,turn):
        for row in range(5,-1,-1):
            if board[row][col] == 0:
                board[row][col] = turn
                return board


    def make_move(self):
        self.turn = self.turn %2 + 1
        player = self.players[self.turn - 1]
        player_move = player.choose_move(self.copy_nest(self.board))
        self.board = self.update_board(self.copy_nest(self.board),player_move,int(self.turn))

    def find_possible_moves(self,board):
        possible_moves = []
        for i in range(len(board[0])):
            if board[0][i] == 0:
                possible_moves.append(i)
        return possible_moves
                

    def is_end(self,board):
        #horizontal
        for row in range(0,6):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                    return str(last_piece)
        #vertical
        for row in range(0,3):
            for col in range(0,7):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                    return str(last_piece)
        #diagonal (\)
        for row in range(0,3):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                    return str(last_piece)
        #diagonal (/)
        for row in range(5,2,-1):
            for col in range(0,4):
                last_piece == board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                    return str(last_piece)
        for row in board:
            if 0 in row:
                return False
        return 'Tie'

    def game(self,log = False):
        while True:
            if log == True:
                self.print_board()
            if self.is_end(list(self.board)) != False:
                return self.is_end(list(self.board))
            self.make_move()
        
            
