import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = y + b 
            dfs(a, y + b)


n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))

# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input().rstrip())
# graph = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))
#     graph[b].append((a, cost))

# def tree_bfs(start:int)->int:
#     dists = [0] * (N+1)
#     dists[start] = 0
#     q = deque([start])
#     while q:
#         now = q.popleft()
#         for node, cost in graph[now]:
#             if dists[node] == 0 and node != start:
#                 dists[node] = dists[now] + cost
#                 q.append(node)
#     return dists

# dists_from_root = tree_bfs(1)
# start = dists_from_root.index(max(dists_from_root))
# result_dists = tree_bfs(start)
# print(dists_from_root, start, result_dists, result_dists.index(max(result_dists)))
# print(max(result_dists))