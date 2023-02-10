import tic_tac_toe as ttt
"""
README FOR FORMATTING: 
    boards are stored as a singular 9 entry array
    children and parents are stored in ID's
    for recombining, nodes are in order of DFS
"""
class TicTacToeTree:
    def __init__(self):
        self.nodes_by_id = {}
        self.nodes_by_state = {}
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
                self.nodes_by_id[node_num] = Node(node_num,new_board,last_node.depth + 1)
                
                #adding children and parents
                self.nodes_by_id[node_num].parents.append(last_node)
                last_node.children.append(self.nodes_by_id[node_num])

                if ttt.is_end_copy(self.nodes_by_id[node_num].board) == False:
                    queue.append(self.nodes_by_id[node_num])
    

    def recursion_recombining_node_tree(self,remaining_depth = 12, node_id = 0):
        if node_id == 0:  
            self.nodes_by_id = {}
            self.nodes_by_id[0] = Node(0,[0 for i in range(0,9)])
            self.nodes_by_state = {}
            self.nodes_by_state[str([0 for i in range(0,9)])] = 0
        #conditional checks
        if remaining_depth != 0 and ttt.is_end_copy(self.nodes_by_id[node_id].board) == False:
        #setup 
            #pre-node creation
            node = self.nodes_by_id[node_id]
            last_move = list(node.board)
            #creates new possible children
            for i in ttt.possible_moves(last_move):
                self.move = 1 if len(ttt.find_all(1,last_move)) == len(ttt.find_all(2,last_move)) else 2
                new_board = list(last_move)
                new_board[i] = self.move
                if str(new_board) in self.nodes_by_state:
                    #don't need to create a new node
                    duplicate_node_id = self.nodes_by_state[str(new_board)]
                    self.nodes_by_id[duplicate_node_id].parents.append(node_id)
                    node.children.append(duplicate_node_id)
                else:
                    new_node_id = len(self.nodes_by_id)
                    self.nodes_by_id[new_node_id] = Node(new_node_id,new_board, node.depth + 1)
                    self.nodes_by_state[str(new_board)] = new_node_id
                    self.nodes_by_id[new_node_id].parents.append(node_id)
                    node.children.append(new_node_id)
                    self.recursion_recombining_node_tree(remaining_depth - 1, new_node_id)
                #everything above here is fine

    def recombining_node_tree(self):
        self.nodes_by_id = {}
        self.nodes_by_id[0] = Node(0,[0 for i in range(0,9)])
        boards = [[0 for i in range(0,9)]]
        queue = [self.nodes_by_id[0]]
        node_num = 0
        while len(queue) != 0:
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
    def __init__(self,node_id,board,depth = 0):
        self.id = node_id
        self.board = board
        self.parents = []
        self.children = []
        self.depth = depth

a = TicTacToeTree()
a.recursion_recombining_node_tree()
