import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] * (n+1) for i in range(n+1)]
result = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque([1])
result[1] = 1
while q:
    now = q.popleft()
    for i in graph[now]:
        if result[i] == 0:
            result[i] = now
            q.append(i)
for i in range(2, n+1):
    print(result[i])