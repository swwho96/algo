import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [[int(10e9)] * K for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

heap = []

def dijkstra(start):
    heappush(heap, [0, start])
    distance[start][0] = 0
    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w     
            if n_w < distance[n_n][K-1]:
                distance[n_n][K-1] = n_w
                distance[n_n].sort()
                heappush(heap, [n_w, n_n])

dijkstra(1)

for i in range(1, N+1):
    if distance[i][K-1] == int(10e9):
        print(-1)
    else:
        print(distance[i][K-1])