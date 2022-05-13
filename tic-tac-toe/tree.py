import tic_tac_toe as ttt
class TicTacToeTree:
    def __init__(self):
        self.nodes_by_id = {}
        self.move = 1

    
    def node_tree(self):
        self.nodes_by_id = {}
        self.nodes_by_id[0] = Node(0,[0 for i in range(9)])
        queue = [self.nodes_by_id[0]]
        node_num = 0
        while len(queue) != 0:
            last_node = queue[0]
            last_move = list(queue[0].board)
            queue.pop(0)
            self.move = 1 if len(ttt.find_all(1,last_move)) == len(ttt.find_all(2,last_move)) else 2
            for i in ttt.possible_moves(last_move):
                node_num += 1
                #making new node

                new_board = list(last_move)
                new_board[i] = self.move
                self.nodes_by_id[node_num] = Node(node_num,new_board)
                
                #adding children and parents
                self.nodes_by_id[node_num].parents.append(last_node)
                last_node.children.append(self.nodes_by_id[node_num])

                if ttt.is_end_copy(self.nodes_by_id[node_num].board) == False:
                    queue.append(self.nodes_by_id[node_num])
    
    def recombining_node_tree(self):
        self.nodes_by_id = {}
        self.nodes_by_id[0] = Node(0,[0 for i in range(0,9)])
        boards = [[0 for i in range(0,9)]]
        queue = [self.nodes_by_id[0]]
        node_num = 0
        while len(queue) != 0:
            print(len(queue))
            last_node = queue[0]
            last_move = list(last_node.board)
            queue.pop(0)
            self.move = 1 if len(ttt.find_all(1,last_move)) == len(ttt.find_all(2,last_move)) else 2
            for i in ttt.possible_moves(last_move):
                new_board = list(last_move)
                new_board[i] = self.move
                if new_board not in boards:
                    boards.append(new_board)
                    node_num += 1
                    self.nodes_by_id[node_num] = Node(node_num,new_board)
                    #children and parents
                    self.nodes_by_id[node_num].parents.append(last_node)
                    last_node.children.append(self.nodes_by_id[node_num])

                    if ttt.is_end_copy(new_board) == False:
                        queue.append(self.nodes_by_id[node_num])

                    
        
class Node:
    def __init__(self,node_id,board):
        self.id = node_id
        self.board = board
        self.parents = []
        self.children = []

a = TicTacToeTree()
a.node_tree()
print(len(a.nodes_by_id))
'''boards = []
failed = []
for i in a.nodes_by_id:
    if a.nodes_by_id[i].board not in boards:
        boards.append(a.nodes_by_id[i].board)
    else:
        print('failed at ',i)
        failed.append(i)
        print('similar to ',boards.index(a.nodes_by_id[i].board))
        print('')
'''