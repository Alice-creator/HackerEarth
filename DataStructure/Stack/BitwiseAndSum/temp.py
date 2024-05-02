count = -1
sum = 0
def And_operation(start, end, arr):
    if start > end:
        return 33554431
    rs = int(arr[start])
    for i in range(start, end):
        rs &= int(arr[i + 1])
    # print(rs)
    return rs
    
T = int(input())
for line in range(T):
    N = int(input())
    temp = input()
    bar = 1
    while bar < N:
        for i in range(-1, N):
            sum += And_operation(0, i, temp) & And_operation(i + 1 + bar, N - 1, temp)
            # print('sum = ', sum, end='\n\n')
        bar += 1
    print(sum)
    sum = 0