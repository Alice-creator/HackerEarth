K, Q = input().split(' ')
K, Q = int(K), int(Q)

HashTable = dict()

def getWeightFromNodeToFather(node):
    father = int(node/K)
    if father not in HashTable:
        return 1
    for i in range(HashTable[father]):
        if i[0] == node:
            return i[1]

for _ in range(Q):
    query = list(map(int, input().split(' ')))
    node1 = query[1]
    node2 = query[2]

    w = query[3] if query[0] == 2 else None
    result = 0
    
    while node1 != node2:
        if w == None:
            result += getWeightFromNodeToFather(node1)
            result += getWeightFromNodeToFather(node2)
            print(result)
        else: