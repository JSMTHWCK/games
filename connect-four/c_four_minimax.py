from c_four_tree import * 
import sys
sys.path.append(sys.path[0] + '/strats')
from strat_custom import custom


class minimaxHeuristic:
    def __init__(self,player,depth):
        self.player = player
        self.depth = depth
        self.generate_new_tree(depth)
        self.scoreClass = custom()

    def generate_new_tree(self,depth):
        self.tree = CFourTree()
        self.tree.recursion_recombining_node_tree(depth)
        self.nodes_by_id = self.tree.nodes_by_id
        self.nodes_by_state = self.tree.nodes_by_state

    def sort_node_by_depth(self,nodes_by_id):
        max_depth = 0
        #finds max depth
        for node in nodes_by_id:
            if max(nodes_by_id[node].depth,max_depth) != max_depth:
                max_depth = nodes_by_id[node].depth
        #sorting
        nodes_by_depth = [[] for _ in range(max_depth + 1)]
        for node in nodes_by_id:
            node_depth = nodes_by_id[node].depth
            nodes_by_depth[node_depth].append(node)
        return nodes_by_depth
    
    def score_heuristic(self,board):
        total_points = 0
        total_points += self.scoreClass.sc_horz(board)
        total_points += self.scoreClass.sc_vert(board)
        total_points += self.scoreClass.sc_ldg(board)    
        #total_points += custom.sc_
        return total_points




    def fit(self):
        nodes_by_depth = self.sort_node_by_depth(self.nodes_by_id)

        #all heuristic values are appended here
        for state_id in nodes_by_depth[-1]:
            state = self.nodes_by_id[state_id]
            current_node = self.nodes_by_id[self.nodes_by_state[str(state.board)]]
            current_node.value = self.score_heuristic(current_node.board)

        for depth in range(len(nodes_by_depth)-2,-1,-1):
            for state_id in nodes_by_depth[depth]:
                state_node = self.nodes_by_id[state_id]
                if len(state_node.children) == 0:
                    state_node.value = self.score_heuristic(current_node.board)
                else:
                    #all minimax-values are appended here
                    turn = CFourTree.find_player_turn(self,state_node.board)
                    children_worth = []

                    for child in state_node.children:
                        children_worth.append(self.nodes_by_id[child].value)
                    state_node.value = max(children_worth) if turn == 1 else min(children_worth)



a = minimaxHeuristic(1,4)
a.fit()
print(len(a.nodes_by_id))
#ignore this




