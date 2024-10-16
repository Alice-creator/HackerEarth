class Node:
    def __init__(self, pre, node, price):
        self.pre = pre
        self.node = node
        self.price = price
        self.next = None

    def __str__(self) -> str:
        result = list()
        node = self
        while node != None:
            result.append(node.node)
            node = node.pre
        
        return f'{self.node} : ' + '->'.join(list(map(str, result[::-1])))

class PriorityQueue:
    def __init__(self):
        self.root = None
    
    def add(self, node):
        if not self.root or node.price <= self.root.price:
            node.next = self.root
            self.root = node
        else:
            temp = self.root
            while temp.price > node.price:
                temp = temp.next
            
            node.next = temp.next
            temp.next = node
    
    def remove(self):
        temp = self.root
        if self.root != None:
            self.root = self.root.next
        return temp

NumOfEdge = int(input())
PQ = PriorityQueue()
routes = dict()
visited = set()
result = list()

for _ in range(NumOfEdge):
    From, To, price = list(map(int, input().split(' ')))
    if From not in routes:
        routes[From] = list()
    if To not in routes:
        routes[To] = list()
    routes[From].append((To, price))
    routes[To].append((From, price))

temp = Node(None,1,0)
while len(visited) < len(routes) and temp != None:
    node = temp.node
    for i in routes[node]:
        if i[0] not in visited and i[0] != node:
            PQ.add(Node(temp, i[0], i[1] + temp.price))
    result.append(temp)
    visited.add(node)
    while temp != None and temp.node in visited:
        temp = PQ.remove()

for i in result:
    print(i)