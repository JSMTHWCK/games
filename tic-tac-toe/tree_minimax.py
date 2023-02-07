from tree import *
def get_key(dict,val):
    for key, value in dict.items():
     if val == value:
        return key

class minimax:
    def __init__(self,player):
        tree = TicTacToeTree()
        self.tree = tree
        tree.recursion_recombining_node_tree()
        self.nodes_by_id = tree.nodes_by_id
        self.nodes_by_state = tree.nodes_by_state
        self.player = player
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
        breakpoint = 0
        self.nodes_by_id = self.tree.nodes_by_id
        nodes_by_depth = self.sort_node_by_depth(self.nodes_by_id)
        for state in nodes_by_depth[-1]:
            breakpoint += 1
            if ttt.is_end_copy(state.board) == "Player " + str(1):
                self.nodes_by_id[self.nodes_by_state[str(state.board)]].value = 1
            elif ttt.is_end_copy(state.board) == 'Tie':
                self.nodes_by_id[self.nodes_by_state[str(state.board)]].value = 0
            else:
                self.nodes_by_id[self.nodes_by_state[str(state.board)]].value = -1
        for depth in range(len(nodes_by_depth) - 2, -1, -1):
            for state_id in nodes_by_depth[depth]:
                breakpoint += 1
                if len(state_id.children) == 0:
                    self.nodes_by_state[str(state_id.board)] = state_id.id
                    if ttt.is_end_copy(state_id.board) == "Player " + str(1):
                        self.nodes_by_id[self.nodes_by_state[str(state_id.board)]].value = 1
                    elif ttt.is_end_copy(state_id.board) == 'Tie':
                        self.nodes_by_id[self.nodes_by_state[str(state_id.board)]].value = 0
                    else:
                        self.nodes_by_id[self.nodes_by_state[str(state_id.board)]].value = -1
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

        print('done')

    def choose_move(self,current_state):
        node_id = self.nodes_by_state[str(current_state)]
        #gets it's children
        children_value = []
        for child_id in self.nodes_by_id[node_id].children:
            children_value.append(self.nodes_by_id[child_id].value)
        best_move = max(children_value) if self.player == 1 else min(children_value)
        #checks for immediate win
        for child_id in self.nodes_by_id[node_id].children:
            if self.player == 1:
                if ttt.is_end_copy(self.nodes_by_id[child_id].board) == "Player 1":
                    return ttt.difference_in_arrays(current_state,self.nodes_by_id[child_id].board)[0]
            else:
                if ttt.is_end_copy(self.nodes_by_id[child_id].board) == "Player 2":
                    return ttt.difference_in_arrays(current_state,self.nodes_by_id[child_id].board)[0]
        #if there are no immediate wins
        move = children_value.index(best_move)
        best_node_id = self.nodes_by_id[node_id].children[move]
        return ttt.difference_in_arrays(current_state,self.nodes_by_id[best_node_id].board)[0]
        


            


