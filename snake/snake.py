import random as rng
from manual import manual
from custom import *
class Game:
    def __init__(self,strat):
        self.strat = strat
        self.board = [['-' for i in range(0,10)] for i in range(0,10)]
        self.berries = 3
        self.snake = [(4,1),(4,2),(4,3)]
        self.berry_location = None
        self.moves = {}
        
    def random_berry(self):
        open_spaces = []
        for i in range(0,10):
            for j in range(0,10):
                if self.board[i][j] == '-':
                    open_spaces.append((i,j))
        self.berry_location = open_spaces[rng.randint(0,len(open_spaces)-1)]

    def find_snake(self):
        snake_segements = []
        for i in range(self.board):
            for j in range(self.board):
                if self.board[i][j] == 'O':
                    snake_segements.append((i,j))
        return snake_segements
    
    def is_end(self):
        #if collides with self
        if len(list(set(self.snake))) != len(self.snake):
            return True
        elif self.snake[-1][0] not in range(0,10):
            return True
        elif self.snake[-1][1] not in range(0,10):
            return True
        return False
    def make_move(self):
        return self.strat(self.board)
    def game(self):
        self.random_berry()
        while True:
            #resets board
            for i in range(0,10):
                for j in range(0,10):
                    self.board[i][j] = '-'
            #update berry
            self.board[self.berry_location[0]][self.berry_location[1]] = 'b'
            #update snake
            for i in self.snake[:-1]:
                self.board[i[0]][i[1]] = 'o'
            i = self.snake[-1]
            self.board[i[0]][i[1]] = 'e'
            #prints board

            for i in self.board:
                print(i)
            print('')
            move = self.make_move()
            mv = None
            if move == 'w':
                mv = (self.snake[-1][0] -1, self.snake[-1][1])
            elif move == 's':
                mv = (self.snake[-1][0] + 1, self.snake[-1][1])
            elif move == 'a':
                mv = (self.snake[-1][0],self.snake[-1][1] - 1)
            elif move == 'd':
                mv = (self.snake[-1][0],self.snake[-1][1] + 1)
            self.snake.append(mv)
            self.moves[mv] =move
            self.snake = self.snake[-self.berries:]
            if self.is_end() == True:
                return self.berries
            if self.berry_location in self.snake:
                self.berries += 1
                print(self.berries)
                self.random_berry()

a = Game(manual)
print(a.game())

