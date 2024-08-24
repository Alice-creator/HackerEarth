T = int(input())

for test in range(T):
    price_list = dict()
    num_list = dict()
    max_bridge = 0
    total_price = 0
    N, M = input().split(' ')
    N, M = int(N), int(M)
    for bridges in range(M):
        name1, name2, price = input().split(' ')

        name = min(int(name1), int(name2)) + max(int(name1), int(name2))
        
        if name in price_list:
            num_list[name] += 1
            price_list[name] += int(price)
        else:
            num_list[name] = 1
            price_list[name] = int(price)
        
        if num_list[name] > max_bridge:
            max_bridge = num_list[name]
        
        total_price += int(price)
    for temp in num_list.keys():
        if max_bridge == num_list[temp]:
            total_price -= price_list[temp]

    print(total_price)