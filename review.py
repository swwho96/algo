import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q = [(0, K)]
distance = [int(10e9)] * (V+1)
distance[K] = 0
while q:
    cost, now = heapq.heappop(q)
    for i in graph[now]:
        if distance[i[0]] > distance[now] + i[1]:
            distance[i[0]] = distance[now] + i[1]
            heapq.heappush(q, (distance[i[0]], i[0]))

for i in range(1, V+1):
    print(distance[i] if distance[i] < int(10e9) else "INF")