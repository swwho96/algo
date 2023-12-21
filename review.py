import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = int(10e9)
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
dist_from_k = [INF] * (V+1)

for i in range(1, E+1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = []
heapq.heappush(q, (0, K))
dist_from_k[K] = 0

while q:
    cost, now = heapq.heappop(q)
    if visited[now] is False:
        visited[now] = True
        for i in graph[now]:
            nnow, ncost = i
            if dist_from_k[nnow] > dist_from_k[now] + ncost:
                dist_from_k[nnow] = dist_from_k[now] + ncost
                heapq.heappush(q, (dist_from_k[nnow], nnow))

for i in range(1, V+1):
    print(dist_from_k[i] if dist_from_k[i] < INF else "INF")