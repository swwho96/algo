from copy import deepcopy
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v, n = map(int, input().split())
    graph[v].append(n)
    graph[n].append(v)

# dfs
dfs_graph = deepcopy(graph)
visited = [True for _ in range(N+1)]
stack = [V]
while stack:
    now = stack.pop()
    if visited[now] is True:
        visited[now] = False
        print(now, end=' ')
        stack += sorted(dfs_graph[now], reverse=True)

print()
# bfs
visited = [True for _ in range(N+1)]
q = [V]
while q:
    now = q.pop(0)
    if visited[now] is True:
        visited[now] = False
        print(now, end=' ')
        for g in sorted(graph[now]):
            if visited[g] is True:
                q.append(g)
