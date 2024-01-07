import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True

cnt = 0
for i in range(1, N+1):
    if visited[i] is False:
        bfs(i)
        cnt += 1

print(cnt)