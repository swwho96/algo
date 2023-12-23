import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = int(10e9)
dist = [INF] * (V+1)
visited = [False] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

q = [(0, K)]
dist[K] = 0
while q:
    cost, now = heapq.heappop(q)
    if visited[now] is False:
        visited[now] = True
        for i in graph[now]:
            nnow, ncost = i
            if dist[nnow] > dist[now] + ncost:
                dist[nnow] = dist[now] + ncost
                heapq.heappush(q, (dist[nnow], nnow))

for i in range(1, V+1):
    print(dist[i] if dist[i] < INF else "INF")