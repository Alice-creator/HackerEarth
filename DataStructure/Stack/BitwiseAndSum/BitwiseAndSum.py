T = None
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
with open('input.txt', 'r') as file:
    for line in file:
        temp = line.split(' ')
        if count < 0:
            T = int(temp[0])
        elif count % 2 == 0:
            N = int(temp[0])
        else:
            bar = 1
            while bar < N:
                for i in range(-1, N):
                    sum += And_operation(0, i, temp) & And_operation(i + 1 + bar, N - 1, temp)
                    # print('sum = ', sum, end='\n\n')
                bar += 1
            print(sum)
        sum = 0
        count += 1