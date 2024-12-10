N, C = list(map(int, input().split()))

ancestors_arr = list(map(int, input().split()))
colors = list(map(int, input().split()))

ancestors_arr.insert(0,0)
colors.insert(0,0)
print(-1, end=' ')
for i in range(1, N + 1):
    ancestor = ancestors_arr[i - 1]
    while colors[i] != colors[ancestor] and ancestor != 0:
        ancestor = ancestors_arr[ancestor - 1]
    
    if ancestor == 0:
        print(-1, end=' ')
    else:
        print(ancestor, end=' ')