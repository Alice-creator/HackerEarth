edges = int(input())
edges_dict = dict()
for i in range(edges):
    u,v,w = list(map(int, input().split()))

    if u not in edges_dict:
        edges_dict[u] = list()
    if v not in edges_dict:
        edges_dict[v] = list()
    
    edges_dict[u].append((v,w))
    edges_dict[v].append((u,w))

heap_queue = list()
disjoint_set = [-1 for i in range(edges)]
visited = set()
MST = list()
current = list(edges_dict.keys())[0]

def add_to_heap(heap, edge_list):
    for i in edge_list:
        heap.append(i)
        index = len(heap) - 1
        print(heap)
        while heap[index][1] < heap[int(index / 2)][1]:
            heap[index], heap[int(index / 2)] = heap[int(index / 2)], heap[index]
            index = int(index / 2)
    return heap

# wrong
def remove_from_heap(heap):
    deleted = heap[0]
    heap[0] = None
    index = 0

    while index < len(heap):
        
        temp_index = index * 2 + 1 if heap[index * 2 + 1][1] > heap[index * 2 + 2][1] else index * 2 + 2
        heap[index], heap[temp_index] = heap[temp_index], heap[index]
        index = temp_index

    return deleted, heap

def union(cur, des):
    root = cur
    while disjoint_set[root] >= 0:
        root = disjoint_set[root]

    temp = disjoint_set[des]
    while True:
        temp = disjoint_set[des]
        disjoint_set[des] = root
        disjoint_set[root] -= 1
        des = temp
        if des < 0:
            break

def check_root(cur, des):
    while disjoint_set[cur] >= 0:
        cur = disjoint_set[cur]
    while disjoint_set[des] >= 0:
        des = disjoint_set[des]
    return cur == des

while len(visited) < edges:
    visited.add(current)
    heap_queue = add_to_heap(heap_queue, edges_dict[current])

    while current in visited:
        (des, w), heap_queue = remove_from_heap(heap_queue)
        if not check_root(current, des):
            union(current, des)
            current = des
            MST.append((current, des))

print(MST)