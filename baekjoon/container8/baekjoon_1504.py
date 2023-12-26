import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

V1, V2 = map(int, input().split())

def dijakstra(start, arrive):
    INF = int(10e9)
    distance = [INF] * (N+1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heapq.heappop(q)
        for i in graph[now]:
            nnow, ncost = i
            if distance[nnow] > distance[now] + ncost:
                distance[nnow] = distance[now] + ncost
                heapq.heappush(q, (distance[nnow], nnow))
    return distance[arrive]

result = min(dijakstra(1, V1) + dijakstra(V1, V2) + dijakstra(V2, N), dijakstra(1, V2) + dijakstra(V2, V1) + dijakstra(V1, N))
print(result if result < int(10e9) else -1)