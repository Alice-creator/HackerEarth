N = int(input())
keypads = list(map(int, input().split()))
keySize = int(input())
keySizes = list(map(int, input().split()))

pointer = [0, 1] #index, value
result = 0
if sum(keySizes) < N:
    print(-1)
else:
    while len(keypads) > 0:
        maxKey = max(keypads)
        keypads.remove(maxKey)
        result += maxKey * pointer[1]

        keySizes[pointer[0]] -= 1

        while True:
            print(pointer, keySizes)
            if pointer[0] + 1 >= len(keySizes):
                pointer = [0, pointer[1] + 1]
            else:
                pointer[0] += 1
            print(pointer, keySizes)
            if keySizes[pointer[0]] > 0:
                break
print(result)