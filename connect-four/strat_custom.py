class custom:
    def __init__(self):
        self.game_turn = None
        self.player = None
    def open_columns(self,board):
        open_col = []
        for i in range(board[0]):
            if i == 0:
                open_col.append(i)
        return open_col

    def get_all(self,board,index):
        ind = []
        for i in range(len(board)):
            if i == index:
                ind.append(i)
        return ind

    def nest_copy(self,board):
        new_list = []
        for i in board:
            new_list.append(i)
        return new_list

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
        for i in self.open_columns:
            if i == 3:
                scores.append(self.fake_boards(self.nest_copy(board),i) * 5)
            else:
                scores.append(self.fake_boards(self.nest_copy(board),i))
        return self.open_columns[scores.index[max(scores)]]

    def fake_boards(self,board):
        pass

    def sc_horz(self,board,plr):
        tot = 0
        for i in range(0,len(board)):
            for j in range(0,len(board[0]) -4):
                nboard = board[i][j:j+4]
                a = self.get_all(nboard,self.player)
                if a == 4:
                    tot += 100
                if a == 3 and 0 in board:
                    tot += 15
                if a == 2 and 0 in board:
                    tot += 7
        return tot

    def sc_vert(self,board):
        for i in range(0,len(board) - 4):
            for j in range(0,len(board[0])):
                arr = []
                for a in range(4):
                    arr.append(board[i+a][j])
                a = self.get_all(arr,self.player)
                if a == 4:
                    tot += 100
                if a == 3 and 0 in board:
                    tot += 15
                if a == 2 and 0 in board:
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
                a = self.get_all(arr,self.player):
                if a == 4:
                    tot += 100
                if a == 3 and 0 in board:
                    tot += 15
                if a == 2 and 0 in board:
                    tot += 7 
        return tot

        
    def sc_rdg(self,board):
        for i in range(5,2,-1):
            for j in range(0,4):
                arr = []
                for a in range(4):
                    a.append(board[i+a][j-a])
                if last_piece == 0:
                    continue
                elif last_piece == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
                    return str(last_piece)