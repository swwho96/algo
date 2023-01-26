import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
distance = [int(1e9)] * (n+1)
start, end = map(int, input().split())
q = [(0, start)]
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
print(distance[end])