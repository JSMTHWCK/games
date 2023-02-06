"""
ABOUT THE FILE: 
everything here should be only for the minimax.
Any helper functions that can be used by the tree or the game will go in their respective files

"""



from tree import *

class minimax:
    def __init__(self,player,depth):
        self.player = player
        self.depth = depth
        #generates starting tree
        self.tree = TicTacToeTree()
        self.tree.recursion_recombining_node_tree(depth)
        #make tree nodes acessible by self
        self.nodes_by_id = self.tree.nodes_by_id
        self.nodes_by_state = self.tree.nodes_by_state
        #player multipliers is : player 1 maxes, player 2 mins
        self.player_multipliers = [1,-1]
        #self.fit just for the initial

    """ALL GLOBAL HELPERS START HERE"""
    #helpers are made to not use self, eventually will be own file for all tree based project
    def find_key_by_value(self,dict,val):
        for key,value in dict.items():
            if val == value:
                return key
    def find_all_of_value(self,array,value):
        indices_of_value = []
        for i in range(len(array)):
            if array[i] == value:
                indices_of_value.append(i)
        return indices_of_value

    def find_difference_in_array(self,array1,array2):
        differences = []
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                differences.append(i)
        return differences

    """ALL MINIMAX HELPERS"""
    def sort_nodes_by_depth(self,nodes_by_id):
        max_depth = 0
        #finds max depth
        for node in nodes_by_id:
            if max(nodes_by_id[node].depth,max_depth) != max_depth:
                max_depth = nodes_by_id[node].depth
        #sorts nodes into respective depth
        nodes_by_depth = [[] for _ in range(max_depth + 1)]
        for node in nodes_by_id:
            node_depth = nodes_by_id[node].depth
            nodes_by_depth[node_depth].append(nodes_by_id[node])
        return nodes_by_depth

    def get_heuristic_value(self,board):
        heuristic = 0
        multipliers = [1,-1]
        for player in [1,2]:
            #vertical
            for i in range(3):
                if len(self.find_all_of_value([board[i],board[i+3],board[i+6]],player)) == 2:
                    heuristic += 1 * multipliers[player -1]
            #horizontal
            for i in range(3):
                if len(self.find_all_of_value([board[3*i+0],board[3*i + 1],board[3*i + 2]],player)) == 2:
                    heuristic += 1 * multipliers[player - 1]
            #left diagonal
            if len(self.find_all_of_value([board[0],board[4],board[8]],player)) == 2:
                heuristic += 1 * multipliers[player-1]
            #right diagonal
            if len(self.find_all_of_value([board[2],board[4],board[6]],player)) == 2:
                heuristic += 1 * multipliers[player-1]

        return heuristic / 8


    """ALL IMPORTANT FUNCTIONS GO HERE"""
    def fit(self):
        self.nodes_by_id = self.tree.nodes_by_id
        nodes_by_depth = self.sort_nodes_by_depth(self.nodes_by_id)
        #gives each a value
        for state in nodes_by_depth[-1]:
            board = state.board
            node_id = self.nodes_by_state[str(board)]
            #absolutes
            if "Player" in str(ttt.is_end_copy(state.board)):
                turn = 1 if self.find_all_of_value(state.board,1) == self.find_all_of_value(state.board,2) else 2
                self.nodes_by_id[node_id].value = 1 * turn
            #heuristics
            else:
                self.nodes_by_id[node_id].value = self.get_heuristic_value(state.board)
        for depth in range(len(nodes_by_depth) -2, -1,-1):
            for state in nodes_by_depth[depth]:
                ##issue is node 1090, has no value
                turn = 1 if self.find_all_of_value(state.board,1) == self.find_all_of_value(state.board,2) else 2
                #if it's a terminal node
                if "Player" in str(ttt.is_end_copy(state.board)):
                    self.nodes_by_id[state.id].value = 1 * [1,-1][turn-1]
                elif len(state.children) == 0:
                    self.get_heuristic_value(state.board)
                else:
                    childrens_worth = []
                    for child in state.children:
                        childrens_worth.append(self.nodes_by_id[child].value)
                    #max
                    if turn == 1:
                        state.value = max(childrens_worth)
                    #mini
                    if turn == 2:
                        state.value = min(childrens_worth)


    def choose_move(self,current_state):
        #current state is array
        current_id = self.nodes_by_state[str(current_state)]
        self.tree.add_new_layer(current_id)
        self.tree.add_new_layer(current_id)
        self.fit()
        #find next best move
        children_ids = []
        children_values = []

        current_node = self.nodes_by_id[current_id]
        for child in current_node.children:
            children_ids.append(child)
            children_values.append(self.nodes_by_id[child].value)
        player_multipliers = [1,-1]
        #immediate wins / losses
        if player_multipliers[self.player - 1] in children_values:
            possible_wins = self.find_all_of_value(children_values,player_multipliers[self.player-1])
            for child_index in possible_wins:
                if ttt.is_end_copy(self.nodes_by_id[children_ids[child_index]].board) == "Player " + str(self.player):
                    return self.find_difference_in_array(current_state,possible_wins[child_index])[0]

        if player_multipliers[self.player - 1] * -1 in children_values:
            index_to_block = children_ids[children_values.index(player_multipliers[self.player - 1]*-1)]
            return index_to_block
        #everything else is heuristic
        if self.player == 1:
            index = children_values.index(max(children_values))

        if self.player == 2:
            index = children_values.index(min(children_values))
        state_board = self.nodes_by_id[children_ids[index]].board
        return self.find_difference_in_array(current_state,state_board)[0]
            
        



