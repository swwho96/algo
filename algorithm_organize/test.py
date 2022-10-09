def dfs(graph, v, visited):
    visited[v] = False
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] is True:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    stack = [v]
    while stack:
        now = stack.pop(0)
        print(now, end=' ')
        visited[now] = False
        for i in graph[now]:
            if visited[i] is True:
                visited[i] = False
                stack.append(i)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [True for _ in range(len(graph))]
dfs(graph, 1, visited)
print()
visited = [True for _ in range(len(graph))]
bfs(graph, 1, visited)