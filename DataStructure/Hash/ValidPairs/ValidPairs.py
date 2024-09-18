# Complete
def solve (N, wealth):
    Arr = wealth
    firstMax = 0
    SecondMax = 0
    temp = 3
    setTemp = [temp]
    dictTemp = dict()
    result = 0

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

    maximun = firstMax + SecondMax

    while maximun > temp:
        temp *= 3
        setTemp.append(temp)

    for i in Arr:
        for j in setTemp:
            if (j - i) in dictTemp:
                result += dictTemp[(j - i)]

    return (int(result / 2))

N = int(input())
wealth = list(map(int, input().split()))

out_ = solve(N, wealth)
print (out_)