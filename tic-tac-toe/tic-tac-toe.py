class Player:
    def __init__(self,player):
        self.player = player

class Game:
    def __init__(self,player1,player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.players = [self.player1,self.player2]
        self.turn = 0
        self.board = [[0 for a in range(3)] for a in range(3)]
