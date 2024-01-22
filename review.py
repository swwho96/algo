from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
result = [0] * (N+1)
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] is False:
                result[i] = now
                q.append(i)
                visited[i] = True

bfs(1)
for i in range(2, N+1):
    print(result[i])