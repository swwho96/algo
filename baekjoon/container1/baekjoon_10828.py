N = int(input())
stack = []
for _ in range(N):
    com = input()
    if com.startswith('push'):
        com, num = com.split()
        stack.append(int(num))
    elif com == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif com == 'size':
        print(len(stack))
    elif com == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif com == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)