import numpy as np
import c_four
def score_heuristic(board):
    #score stuff
    scores = [0,1,7,15,np.inf]
    total_points = 0
    #scores vertical
    if len(board) > 4:
        for i in range(0,len(board) - 3):
            for j in range(0,len(board[0])):
                subboard = []
                for a in range(4):
                    subboard.append(board[i+a][j])
                total_points += scores[subboard.count(1)] * [1,-1][0]
                total_points += scores[subboard.count(2)] * [1,-1][1] 
    #scores horizontal
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            subboard = board[i][j:j+4]
            total_points += scores[subboard.count(1)] * [1,-1][0]
            total_points += scores[subboard.count(2)] * [1,-1][1]
    #scores left diagonal 
    if len(board) > 4:
        for i in range(0,len(board) - 4):
            for j in range(0,len(board[0]) - 4):
                subboard = []
                for a in range(4):
                    subboard.append(board[i+a][j+a])
                
                total_points += scores[subboard.count(1)] * [1,-1][0]
                total_points += scores[subboard.count(2)] * [1,-1][1]
    #scores right diagonal
    if len(board) > 4:
        for row in range(5,2,-1):
            for col in range(0,4):
                subboard = [board[row][col],board[row-1][col+1], board[row-2][col+2], board[row-3][col+3]]
                total_points += scores[subboard.count(1)] * [1,-1][0]
                total_points += scores[subboard.count(2)] * [1,-1][1]
    return total_points
print(score_heuristic(
  [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0], [1, 0, 0, 2, 0, 0, 0], [1, 0, 1, 2, 2, 0, 1], [1, 0, 1, 2, 2, 2, 1]]
))