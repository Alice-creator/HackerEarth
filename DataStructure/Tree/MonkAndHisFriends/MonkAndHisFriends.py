T = int(input())

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

for i in range(T):
    N,M = list(map(int, input().split()))
    Arr = list(map(int, input().split()))

    root = Node(Arr.pop(0))
    for j in range(N - 1):
        temp = root
        while temp != None:
            if temp.key < Arr[j]:
                if temp.right != None:
                    temp = temp.right
                else:
                    temp.right = Node(Arr[j])
                    break

            elif temp.key > Arr[j]:
                if temp.left != None:
                    temp = temp.left
                else:
                    temp.left = Node(Arr[j])
                    break
            else:
                break
    
    for j in range(N - 1, N - 1 + M):
        temp = root
        while temp != None:
            if temp.key < Arr[j]:
                if temp.right != None:
                    temp = temp.right
                else:
                    temp.right = Node(Arr[j])
                    break
            elif temp.key > Arr[j]:
                if temp.left != None:
                    temp = temp.left
                else:
                    temp.left = Node(Arr[j])
                    break
            else:
                break
        
        if temp.key == Arr[j]:
            print('YES')
        else:
            print('NO')