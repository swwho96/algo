from queue import deque
N = int(input())
stack = deque([])
for _ in range(N):
    com = input()
    if com.startswith('push'):
        com, num = com.split()
        stack.append(int(num))
    elif com == 'pop':
        if len(stack) > 0:
            print(stack.popleft())
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