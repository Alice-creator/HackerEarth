class priorityQ:
    def __init__(self):
        self.root = None
        self.next = None
    
    def addNode(self, node):
        if not self.root:
            self.root = node
        else:
            

N,M,A,B = list(int, input().split(' '))
paper_map = dict()
stamina_map = dict()
visited = set()
unvisited = set()
Q = list()

stamina = 0
hours = 0

for _ in range(M):
    X, Y, Z = list(int, input().split(' '))
    if X not in paper_map:
        paper_map[X] = list()
        unvisited.add(X)
    if Y not in paper_map:
        paper_map[Y] = list()
        unvisited.add(Y)

    paper_map[X].append((Y, Z))
    paper_map[Y].append((X, Z))

for _ in range(N):
    C, H = list(int, input().split(' '))
    stamina_map[C] = H

while len(unvisited) != 0:
    for i in paper_map[A]:
        temp = (i[0], A, i[1])
        