import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] is False:
                visited[i] = True
                q.append(i)

# def dfs(start):
#     stack = [start]
#     visited[start] = True
#     while stack:
#         now = stack.pop()
#         print(now, end=' ')
#         for i in graph[now]:
#             if visited[i] is False:
#                 visited[i] = True
#                 dfs(i)
def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        now = stack.pop()
        print(now, end=' ')
        for i in sorted(graph[now], reverse=True):
            if visited[i] is False:
                visited[i] = True
                stack.append(i)

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)