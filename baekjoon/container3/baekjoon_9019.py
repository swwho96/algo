import sys
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = sys.stdin.readline().split()
    A = '0' * (4-len(A)) + A
    B = '0' * (4-len(B)) + B
    q = [('', A)]
    visited = [False] * 10001
    while q:
        op, num = q.pop(0)
        if num == B: # B가 되었다면 종료
            print(op)
            break

        D_num = str((2*int(num)) % 10000)
        D_num = '0' * (4-len(D_num)) + D_num
        if not visited[int(D_num)]:
            visited[int(D_num)] = True
            q.append((op+'D', D_num))

        S_num = '9999' if num == '0000' else str(int(num)-1)
        S_num = '0' * (4-len(S_num)) + S_num
        if not visited[int(S_num)]:
            visited[int(S_num)] = True
            q.append((op+'S', S_num))

        L_num = num[1:] + num[0]
        if not visited[int(L_num)]:
            visited[int(L_num)] = True
            q.append((op+'L', L_num))

        R_num = num[3] + num[:3]
        if not visited[int(R_num)]:
            visited[int(R_num)] = True
            q.append((op+'R', R_num))

# ---------------------------------------------------------------------

import sys
from collections import deque
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    q = deque([('', A)])
    visited = [False] * 10001
    while q:
        op, num = q.popleft()
        if num == B: # B가 되었다면 종료
            print(op)
            break
        left, right = num // 1000, num % 10
        d = (num*2) % 10000
        s = 9999 if num == 0 else (num-1)
        l = ((num*10)+left) % 10000
        r = (right*1000) + (num//10)

        for n, c in zip([d,s,l,r], ['D','S','L','R']):
            if not visited[n]:
                visited[n] = True
                q.append((op+c, n))