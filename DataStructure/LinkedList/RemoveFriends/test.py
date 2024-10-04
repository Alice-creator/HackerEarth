class node:
    def __init__(self, next = None, pre = None, value = None):
        self.next = next
        self.value = value
        self.pre = pre

T = int(input())

for test in range(T):
    N, K = input().split(' ')
    N, K = int(N), int(K)
    popularities = list(map(int, input().split()))
    i = 1
    length = len(popularities) - K
    root = node(value=popularities[0])
    temp = root
    for i in range(1, len(popularities)):
        temp.next = node(pre=temp, value=popularities[i])
        temp = temp.next
    
    temp = root
    while temp.next != None and K > 0:    
        if temp.value < temp.next.value:
            K -= 1
            if temp != root:
                temp.pre.next = temp.next
                temp = temp.pre
            else:
                root = temp.next
                temp = root
        else:
            temp = temp.next
    
    for i in range(length):
        print(temp.value, end=' ')
        temp = temp.next
    print()