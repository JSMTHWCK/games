from tree import *
from run_game import *
def get_key(dict,val):
    for key, value in dict.items():
     if val == value:
        return key

class minimax:
    def __init__(self,player,depth):
        self.player = player
        self.depth = depth
        self.generate_new_tree(depth)

    def get_all(self,array,index):
        ind = []
        for i in range(len(array)):
            if i == index:
                ind.append(i)
        return ind

    def generate_new_tree(self,depth,starting_node = 0):
        self.tree = TicTacToeTree()
        self.tree.recursion_recombining_node_tree(depth,starting_node)

        self.nodes_by_id = self.tree.nodes_by_id
        self.nodes_by_state = self.tree.nodes_by_state

        self.fit()

    def find_key_by_value(self,dict,val):
        for key, value in dict.items():
            if val == value:
                return key
    def sort_node_by_depth(self,nodes_by_id):
        max_depth = 0
        #finds max depth
        for node in nodes_by_id:
            if max(nodes_by_id[node].depth,max_depth) != max_depth:
                max_depth = nodes_by_id[node].depth
        #sorting
        nodes_by_depth =  [[] for i in range(max_depth + 1)]
        for node in nodes_by_id:
            node_depth = nodes_by_id[node].depth
            nodes_by_depth[node_depth].append(nodes_by_id[node])
        return nodes_by_depth
            
    def fit(self):
        self.nodes_by_id = self.tree.nodes_by_id
        nodes_by_depth = self.sort_node_by_depth(self.nodes_by_id)
        #gives each a value
        for state in nodes_by_depth[-1]:
            #absolute stuff
            if ttt.is_end_copy(state.board) == "Player 1":
                self.nodes_by_id[self.nodes_by_state[str(state.board)]].value = 1
            elif ttt.is_end_copy(state.board) == 'Tie':
                self.nodes_by_id[self.nodes_by_state[str(state.board)]].value = 0
            elif ttt.is_end_copy(state.board) == "Player 2":
                self.nodes_by_id[self.nodes_by_state[str(state.board)]].value = -1
            #heuristic stuff
            else:
                continue
        for depth in range(len(nodes_by_depth) - 2, -1, -1):
            for state_id in nodes_by_depth[depth]:
                #if another terminal node
                if len(state_id.children) == 0:
                    self.nodes_by_state[str(state_id.board)] = state_id.id
                    #absolute states
                    if ttt.is_end_copy(state_id.board) == "Player 1":
                        self.nodes_by_id[self.nodes_by_state[str(state_id.board)]].value = 1
                    elif ttt.is_end_copy(state_id.board) == 'Tie':
                        self.nodes_by_id[self.nodes_by_state[str(state_id.board)]].value = 0
                    elif ttt.is_end_copy(state_id.board) == "Player 2":
                        self.nodes_by_id[self.nodes_by_state[str(state_id.board)]].value = -1
                    #heuristic part goes here
                    else:
                        continue

                #if children have values (and exist)
                else:
                    turn = 1 if len(ttt.find_all(1,state_id.board)) == len(ttt.find_all(2,state_id.board)) else 2
                    childrens_worth = []
                    for child in state_id.children:
                        childrens_worth.append(self.nodes_by_id[child].value)
                    #maximizing
                    if turn == 1:
                        state_id.value = max(childrens_worth)
                    #minimizing
                    if turn == 2:
                        state_id.value = min(childrens_worth)

        #print('done')

    def choose_move(self,current_id):
        #just generating a new tree basically
        self.tree.add_new_layer(current_id)
        self.fit()
        
        #finds next best move
        children = []
        childrens_value = []
        #all value populating goes here
        current_node = self.nodes_by_id[current_id]
        for child in current_node.children:
            children.append(child)
            childrens_value.append(current_node[child].value)
        #if guarenteed wins (1) or immediate losses (-1)
        player_multiplier = 1 if len(ttt.find_all(1,current_node.board)) == len(ttt.find_all(2,current_node.board)) else -1
        if 1 * player_multiplier in childrens_value:
            #checks for immediate wins
            possible_wins = self.tree.find_all(childrens_value[1])
            for child in possible_wins:
                if ttt.is_end_copy(self.nodes_by_id[child].board) == "Player 1" and player_multiplier == 1:
                    return child
                elif ttt.is_end_copy(self.nodes_by_id[child].board) == "Player 2" and player_multiplier == -1:
                    pass

            
        elif -1 * player_multiplier in childrens_value:
            return children[childrens_value.index(-1)]
        #find child with highest (or lowest if p2) heuristic value
        if player_multiplier == 1:
            return children[childrens_value.index(max(childrens_value))]
        else:
            return children[childrens_value.index(min(childrens_value))]


            
"""Otherwise, count up the number of rows, columns, and diagonals where you occupy two spaces and the third space is empty. 
Then, subtract the number of rows, columns, and diagonals where your opponent occupies two spaces and the third space is empty. 
Finally, divide the result by 8 (which is the total number of rows, columns, and diagonals)."""

def add_new_layer(self,starting_id):
    #starts with "pruning the tree"
    self.prune_tree(starting_id)
    #finds terminal node
    queue = []
    for node_id in self.nodes_by_id:
        if self.nodes_by_id[node_id].children == []:
            queue.append(node_id)
    for node_id in queue:
        last_move = list(self.nodes_by_id[node_id])
        node = self.nodes_by_id[node]
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
        queue.pop(0)
    



def prune_tree(self,starting_id):
    #updates both nodes_by_id and 
    new_nodes_by_id = {}
    new_nodes_by_state = {}
    queue = [starting_id]
    while len(queue) != 0:
        node_id = int(queue[0])
        queue.pop(0)
        print(len(queue))
        new_nodes_by_id[node_id] = self.nodes_by_id[node_id]
        new_nodes_by_state[str(self.nodes_by_id[node_id].board)] = self.nodes_by_state[str(self.nodes_by_id[node_id].board)]
        for child in self.nodes_by_id[node_id].children:
            queue.append(child)
    print(len(new_nodes_by_id))
    print(len(self.nodes_by_id))
    self.nodes_by_id = new_nodes_by_id
    self.nodes_by_state = new_nodes_by_state
