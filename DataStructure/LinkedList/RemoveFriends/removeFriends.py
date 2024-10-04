# Done
T = int(input())

for test in range(T):
    N, K = input().split(' ')
    N, K = int(N), int(K)
    popularities = list(map(int, input().split()))
    stack = list()

    for i in popularities:
        while len(stack) > 0 and stack[-1] < i and K > 0:
            stack.pop()
            K -= 1
        stack.append(i)
    
    for i in stack:
        print(i, end=' ')
    print()