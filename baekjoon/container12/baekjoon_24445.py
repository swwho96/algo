import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
lines = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    lines[u].append(v)
    lines[v].append(u)

for l in lines:
    l.sort(reverse=True)

q = deque([R])
order = 1
answer = [-1] * (N+1)
answer[R] = 1
while q:
    now = q.popleft()
    for i in lines[now]:
        if answer[i] == -1:
            order += 1
            answer[i] = order
            q.append(i)

for i in range(1,N+1):
    print(answer[i] if answer[i] != -1 else 0)