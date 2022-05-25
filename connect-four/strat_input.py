class manual:
    def choose_move(self,board):
        a = input()
        while a not in ['0','1','2','3','4','5','6']:
            print("invalid input, please choose 0 - 6 (indexed at 0)")
            a = input()
        return int(a)