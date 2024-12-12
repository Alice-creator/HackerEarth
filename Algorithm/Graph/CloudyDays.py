cities, roads, fuels, current = list(map(int, input().split()))

road_dict = dict()

for i in range(roads):
    u,v = list(map(int, input().split()))
    if u not in road_dict:
        road_dict[u] = list()
    if v not in road_dict:
        road_dict[v] = list()
    road_dict[u].append(v)
    road_dict[v].append(u)

queue_to_visit = list()
visited = set()

while fuels > 0 and len(visited) < cities:
    queue_to_visit.extend(road_dict[current])
    visited.add(current)
    fuels -= 1
    while current in visited and len(queue_to_visit) > 0:
        current = queue_to_visit.pop(0)

print(len(visited | set(queue_to_visit) | {current}))