import sys
M = int(sys.stdin.readline().rstrip())
S = set()
for _ in range(M):
    command = sys.stdin.readline().rstrip().split()
    if command[-1].isdigit():
        command, x = command.split()
        x = int(x)
    if command == 'add':
        S.add(x)
    elif command == 'remove' and x in S:
        S.remove(x)
    elif command == 'check':
        sys.stdout.write('1' + '\n' if x in S else '0'+'\n')
    elif command == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif command == 'all':
        S = set((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
    elif command == 'empty':
        S.clear()