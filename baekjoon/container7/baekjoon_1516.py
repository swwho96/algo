import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
v = [0] * (n+1)
g = [[] for _ in range(n+1)]
cost = [0] * (n+1)
result = [0] * (n+1)
for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    cost[i] += tmp[0]
    for t in tmp[1:-1]:
        g[t].append(i)
    v[i] += len(tmp[1:-1])

q = deque([])
for i in range(1,n+1):
    if v[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in g[now]:
        v[i] -= 1
        result[i] = max(result[i], result[now]+cost[now])
        if v[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i] + cost[i])