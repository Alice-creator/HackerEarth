def mod_left(x, m):
    return x**2 % m

def mod_right(x, a,b,c,d,m):
    return (a*x**3 + b*x**2 + c*x + d) % m

T = int(input())

for i in range(T):
    hash_dict_left = dict()
    hash_dict_right = dict()
    a,b,c,d,m = list(map(int, input().split()))
    arr_len = int(input())
    arr = list(map(int, input().split()))
    for j in arr:
        modLeft = mod_left(j, m)
        modRight = mod_right(j, a,b,c,d,m)
        if modLeft not in hash_dict_left:
            hash_dict_left[modLeft] = list()
        if modRight not in hash_dict_right:
            hash_dict_right[modRight] = list()

        hash_dict_left[modLeft].append(j)
        hash_dict_right[modRight].append(j)

    result = 0
    for j in hash_dict_left.keys():
        if j in hash_dict_right:
            # print(j)
            # print(hash_dict_left[j],hash_dict_right[j])
            result += len(hash_dict_left[j])*len(hash_dict_right[j])
    print(result)