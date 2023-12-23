import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indgree[b] += 1

q = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        q.append(i)
    
result = []
while q:
    now = q.popleft()
    result.append(str(now))
    for i in graph[now]:
        indgree[i] -= 1
        if indgree[i] == 0:
            q.append(i)

print(' '.join(result))