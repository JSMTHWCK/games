from strat_custom import custom
from c_four_tree import CFourTree as cft

static_custom = custom()
score = static_custom.score_board

class minimax:
    def __init__(self,player,depth):
        self.tree_class = cft()
        #do some tree stuff here
        self.player = player
        self.depth = depth
    def generate_tree(self,starting_node,depth):
        self.tree = self.tree_class.recursion_recombining_node_tree(depth,starting_node)
    
    def find_key_by_value(self,dict,val):
        for key,value in dict.items():
            if val == value:
                return key
    def sort_node_by_depth(self,nodes_by_id):
        nodes_by_depth = [[] for i in range(self.depth + 1)]
        for node_id in nodes_by_id:
            node_depth = nodes_by_id[node_id].depth
            nodes_by_depth[node_depth].append(nodes_by_id[node_id])
        return nodes_by_depth

    def fit(self,tree_depth):
        pass
    def choose_move(self,current_state):
        #all the pre-searching stuff
        node_id = self.nodes_by_state[str(current_state)]
        self.generate_tree(self,node_id,self.depth)


        #actual searching