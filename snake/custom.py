'''
import csv
file = open('snake_node.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)
'''
class Node:
    def __init__(self,id):
        self.id = id
        self.parents = []
        self.children = []
        self.visited = {}
    def nest_copy(self,board):
        new_board = []
        for i in board:
            new_board.append(list(i))
        return new_board
    def add_children(self,id,valid_moves):
        self.children = []
        for i in valid_moves:
            if i[0] == id:
                self.children.append(i[1])
    def add_parents(self,id,valid_moves):
        self.parents = []
        for i in valid_moves:
            if i[1] == id:
                self.parents.append(i[0])

    
            


df_hamiltonian = {
    #will be the excel file
}
#populate family works now
def populate_family(valid_moves):
    nid = {}
    for i in valid_moves:
        nid[i[0]] = Node(i[0])
        nid[i[1]] = Node(i[1])
    for i in nid:
        nid[i].add_children(i,valid_moves)
        nid[i].add_parents(i,valid_moves)
    return nid

valid_moves = [
    (0,1), (1,0),
    (1,2), (2,1),
    (2,4), (4,2),
    (1,3), (3,1),
    (1,4), (4,1),
    (0,3), (3,0),
    (3,4), (4,3)
]

nid = populate_family(valid_moves)
'''
for i in nid:
    print('i is ',i)
    print(nid[i].children)
    print(nid[i].parents)
    print('')
'''
