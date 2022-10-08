N = int(input())
stack = []
for _ in range(N):
    com = input()
    if com.startswith('push_front'):
        com, num = com.split()
        stack = [int(num)] + stack
    elif com.startswith('push_back'):
        com, num = com.split()
        stack += [int(num)]
    elif com == 'pop_front':
        if len(stack) > 0:
            print(stack[0])
            stack = stack[1:]
        else:
            print(-1)
    elif com == 'pop_back':
        if len(stack) > 0:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)
    elif com == 'size':
        print(len(stack))
    elif com == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if len(stack) > 0:
            print(stack[0])
        else:
            print(-1)
    elif com == 'back':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)