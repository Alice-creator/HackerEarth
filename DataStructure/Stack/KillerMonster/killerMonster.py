import sys

iteration = int(sys.stdin.readline().rstrip())

for i in range(iteration):
    monster_num = int(sys.stdin.readline().rstrip())
    monster = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(' ')))
    stack = [monster[0]]

    for j in monster:
        while len(stack) > 0 and stack[-1] <= j:
            stack.pop()
        stack.append(j)
        sys.stdout.write(str(len(stack)) + ' ')
    sys.stdout.write('\n')