import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = [False] * (N+1)
def dfs(start, cnt):
    global answer
    if cnt >= 5:
        answer = 1
        return
    visited[start] = True
    for i in graph[start]:
        if visited[i] is False:
            dfs(i, cnt+1)
    visited[start] = False

for i in range(1, N+1):
    dfs(i, 1)
    if answer == 1:
        break

print(answer)