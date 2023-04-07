import copy as copy
class custom:
    def __init__(self):
        self.game_turn = None
        self.player = None
    def open_columns(self,board):
        open_col = []
        for i in range(len(board[0])):
            if board[0][i] == 0:
                open_col.append(i)
        return open_col

    def get_all(self,board,index):
        ind = []
        for i in range(len(board)):
            if i == index:
                ind.append(i)
        return ind


    def choose_move(self,board):
        if self.game_turn == None:
            if board[-1] == [0 for i in range(7)]:
                self.game_turn = 0
                self.player = 1
            if 1 in board[-1] and 2 not in board:
                self.game_turn = 0
                self.player = 2
        self.game_turn += 1
        if self.game_turn == 1:
            return 3
        if self.game_turn == 2 and self.player == 1:
            if 2 not in board[-1]:
                #implies they stacked 3
                return 2
            else:
                return 3
        if self.game_turn == 3 and self.player == 1:
            if board[-2][3] == 1:
                if board[-3][3] != 2:
                    return 2
            if 2 not in board[-1]:
                return 1
                #traps them into the 2 ends
            else:
                return board[-1].index(2)
        scores = []
        for i in self.open_columns(copy.deepcopy(board)):
            if i == 3:
                scores.append(self.fake_boards(copy.deepcopy(board),i) * 5)
            else:
                scores.append(self.fake_boards(copy.deepcopy(board),i))

        return self.open_columns(board)[scores.index(max(scores))]

    def fake_boards(self,board,index):
        new_board = copy.deepcopy(board)
        for i in range(5,-1,-1):
            if new_board[i][index] == 0:
                new_board[i][index] = self.player
                break
        tot = 0
        tot += self.sc_horz(new_board)
        tot += self.sc_vert(new_board)
        tot += self.sc_ldg(new_board)
        #tot += self.sc_rdg(board)
        return tot

        

    def sc_horz(self,board):
        tot = 0
        for i in range(0,len(board)):
            for j in range(0,len(board[0]) -4):
                arr = board[i][j:j+4]
                a = 4 - len(self.get_all(arr,1))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in arr:
                    tot += 15
                if a == 2 and 0 in arr:
                    tot += 7
                a = 4 - len(self.get_all(arr,2))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in arr:
                    tot += 15
                if a == 2 and 0 in arr:
                    tot += 7
        return tot

    def sc_vert(self,board):
        tot = 0
        for i in range(0,len(board) - 4):
            for j in range(0,len(board[0])):
                arr = []
                for a in range(4):
                    arr.append(board[i+a][j])
                a = 4 - len(self.get_all(arr,1))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in arr:
                    tot += 15
                if a == 2 and 0 in arr:
                    tot += 7
                a = 4 - len(self.get_all(arr,2))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in arr:
                    tot += 15
                if a == 2 and 0 in arr:
                    tot += 7
        return tot
        
    def sc_ldg(self,board):
        #\
        tot = 0
        for i in range(0,len(board) - 4):
            for j in range(0,len(board[0]) - 4):
                arr = []
                for a in range(4):
                    arr.append(board[i+a][j+a])
                a = 4 - len(self.get_all(arr,1))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in arr:
                    tot += 15
                if a == 2 and 0 in arr:
                    tot += 7
                a = 4 - len(self.get_all(arr,2))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in arr:
                    tot += 15
                if a == 2 and 0 in arr:
                    tot += 7
        return tot

        
    def sc_rdg(self,board):
        tot = 0
        for i in range(5,2,-1):
            for j in range(0,4):
                arr = []
                for a in range(4):
                    arr.append(board[i+a][j-a])
                a = len(self.get_all(arr,self.player))
                if a == 4:
                    tot += 100
                if a == 3 and 0 in board:
                    tot += 15
                if a == 2 and 0 in board:
                    tot += 7
                
        return tot