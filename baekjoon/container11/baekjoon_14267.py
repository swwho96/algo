import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [0]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(2, N+1):
    graph[i].append(parents[i])
    graph[parents[i]].append(i)

result = [0] * (N+1)
def dfs(start:int, w:int):
    for node in graph[start]:
        if node != parents[start]:
            result[node] += result[start]
            dfs(node, result[node])

for _ in range(M):
    s, w = map(int, input().split())
    result[s] += w
dfs(2, result[2])

print(' '.join(map(str, result[1:])))