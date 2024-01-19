import heapq
import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
start, end = map(int, input().split())

q = [(0, start)]
distance = [int(10e9)] * (V+1)
distance[start] = 0
while q:
    cost, now = heapq.heappop(q)
    for i in graph[now]:
        if distance[i[0]] > distance[now] + i[1]:
            distance[i[0]] = distance[now] + i[1]
            heapq.heappush(q, (distance[i[0]], i[0]))   

print(distance[end])