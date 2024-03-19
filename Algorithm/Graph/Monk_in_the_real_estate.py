import numpy as np

T = int(input())

# print(arr)
while T > 0:
    E = int(input())
    count = 0
    arr = np.zeros(shape=(10001))
    for i in range(E):
        temp = input().split(' ')
        for j in temp:
            if arr[int(j)] == 0:
                arr[int(j)] = 1
                count += 1

    print(count)

    T -= 1