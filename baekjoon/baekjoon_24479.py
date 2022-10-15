import sys

N, M, R = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [R]
visited = [False for _ in range(N+1)]
visit_time = [0 for _ in range(N+1)]
time = 1
while stack: # dfs
    now = stack.pop()
    if visited[now] is False:
        visited[now] = True
        visit_time[now] = time
        time += 1
        stack.extend(sorted(graph[now], reverse=True))

for i in range(1, N+1):
    print(visit_time[i])