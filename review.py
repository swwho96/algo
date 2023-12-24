import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
for _ in range(E):
    edges.append(list(map(int, input().split())))

INF = int(10e9)
distance = [INF] * (V+1)
distance[1] = 0

for _ in range(V-1):
    for s, e, t in edges:
        if distance[s] != INF and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

cycle = False
for s, e, t in edges:
    if distance[s] != INF and distance[e] > distance[s] + t:
        cycle = True
        break

if cycle is False:
    for i in range(2, V+1):
        print(distance[i] if distance[i] != INF else -1)
else:
    print(-1) 