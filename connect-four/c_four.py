from manual import *
class Game:
    def __init__(self,p_one, p_two):
        self.players = [p_one,p_two]
        self.turn = 0
        self.board = [0 for i in range(42)]

    def convert_to_nest(self,board):
        arr = []
        for a in range(0,6):
            arr_inner = []
            for b in range(0,7):
                arr_inner.append(board[7*a + b])
            arr.append(arr_inner)
        return arr
    def print_board(self):
        a = self.convert_to_nest(self.board)
        for i in a:
            print(i)
            
    def make_move(self,turn):
        a = int(self.players[turn](list(self.board)))
        for i in range(5,-1,-1):
            if self.board[i*7 + a] == 0:
                self.board[i*7 + a] = turn + 1
                break
    def is_end(self):
        nest_board = self.convert_to_nest(list(self.board))
        #horizontal
        for i in range(0,6):
            for j in range(0,4):
                last_piece = nest_board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == nest_board[i][j+1] == nest_board[i][j+2] == nest_board[i][j+3]:
                    return str(last_piece)
        #vertical
        for i in range(0,3):
            for j in range(0,7):
                last_piece = nest_board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == nest_board[i+1][j] == nest_board[i+2][j] == nest_board[i+3][j]:
                    return str(last_piece)
        #diagonal (\)
        for i in range(0,3):
            for j in range(0,4):
                last_piece = nest_board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == nest_board[i+1][j+1] == nest_board[i+2][j+2] == nest_board[i+3][j+3]:
                    return str(last_piece)
        #diagonal (/)
        for i in range(5,2,-1):
            for j in range(0,4):
                last_piece == nest_board[i][j]
                if last_piece == 0:
                    continue
                elif last_piece == nest_board[i-1][j+1] == nest_board[i-2][j+2] == nest_board[i-3][j+3]:
                    return str(last_piece)
        if 0 not in self.board:
            return 'Tie'
        return False
    def game(self,log = False):
        while True:
            if log == True:
                self.print_board()

            if self.is_end() != False:
                return self.is_end()
            self.make_move(self.turn)
            self.turn = (self.turn + 1)%2
a = Game(manual,manual)
print(a.game(log = True))