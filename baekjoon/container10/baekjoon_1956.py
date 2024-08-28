import sys
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[int(10e9)] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    dist[a][b] = c

min_dist = int(10e9)
for i in range(1, V+1):
    dist[i][i] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

for i in range(1, V+1):
    for g in graph[i]:
        min_dist = min(min_dist, dist[i][g]+dist[g][i])

print(min_dist if min_dist < int(10e9) else -1)