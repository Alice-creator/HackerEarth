import math

T = int(input())

for i in range(T):
    N = int(input())
    Arr = [] # Div index, sum
    index = 0
    Dividable = list()

    for j in range(int(math.sqrt(N))):
        if N // j:
            Dividable.append(j)
    Dividable.reverse()

    while len(Arr) < 4:
        if index < len(Dividable):
            Arr.append([index, Dividable[index]])

        if len(Arr) == 4 and Arr[-1][1] == N:
            break
        elif len(Arr) == 4 or Arr[-1][1] >= N:
            Arr.pop()
            temp = Arr.pop()
            if temp[0] + 1 < len(Dividable):
                index = temp[0] + 1
            else:
                index = 0
        else:
            index = 0