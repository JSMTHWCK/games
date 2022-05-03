class Game:
    def __init__(self,p_one, p_two):
        self.player1 = p_one
        self.player2 = p_two
        self.players = [self.player1,self.player2]
        self.turn = 0
        self.board = ['-' for i in range(42)]
    def convert_to_nest(self,board):
        outer_arr = []
        for i in range(0,6):
            arr = []
            for j in range(0,7):
                arr.append(self.board[6*i+j])
            outer_arr.append(arr)
        return outer_arr
    def print_board(self):
        arr = self.convert_to_nest(list(self.board))
        for sub_arr in arr:
            print(sub_arr)
    
    def is_end(self):
        board = self.convert_to_nest(list(self.board))
        for i in range(6):
            for j in range(4):
                last_piece = board[i][j]
                if last_piece == '-':
                    continue
                elif last_piece == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                    return last_piece
        
        for i in range(7):
            for j in range(3):
                last_piece = board[i][j]
                if last_piece == '-':
                    continue
                elif last_piece == board[i+1][j] + board[i+2][j] + board[i+3][j]:
                    return last_piece
        
        for i in range(3):
            for j in range(4):
                last_piece = board[i][j]
                if last_piece == '-':
                    continue
                elif last_piece == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                    return last_piece
        
        for i in range(5,2,-1):
            for j in range(4):
                last_piece = board[i][j]
                if last_piece == '-':
                    continue
                elif last_piece == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
                    return last_piece
        return False
    
