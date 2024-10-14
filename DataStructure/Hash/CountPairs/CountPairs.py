T = int(input())
temp = list(map(int, input().split()))
Arr = list(map(int, input().split()))
N = temp[0]
k = temp[1]
p = temp[2]
firstMax = 0
secondMax = 0
dictTemp = {}
alphaList = list()

for _ in T:
    for i in range(len(Arr)):
        if Arr[i] not in dictTemp:
            dictTemp[Arr[i]] = 1
        else:
            dictTemp[Arr[i]] += 1
        if Arr[i] > firstMax:
            firstMax = Arr[i]
            continue
        if Arr[i] > SecondMax:
            SecondMax = Arr[i]

    alpha = firstMax + SecondMax

    maxTemp = int((alpha - k) / p)

    for i in range(maxTemp):
        alphaList.append(i*p + k)
    