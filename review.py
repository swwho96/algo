import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

INF = int(10e9)
dist = [INF] * (N+1)

q = [(0, start)]
dist[start] = 0

while q:
    cost, now = heapq.heappop(q)
    if visited[now] is False:
        visited[now] = True
        for i in graph[now]:
            nnow, ncost = i
            if dist[nnow] > dist[now] + ncost:
                dist[nnow] = dist[now] + ncost
                heapq.heappush(q, (dist[nnow], nnow))

print(dist[end])