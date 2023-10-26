import sys
import heapq
input = sys.stdin.readline
V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    tmp = list(map(int, input().split()))
    s = tmp[0]
    for i in range(1, len(tmp)-1, 2):
        tree[s].append((tmp[i+1], tmp[i]))
        tree[tmp[i]].append((tmp[i+1], s))


def dijkstra(start):
    distance = [int(1e9) for _ in range(V+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for i in tree[now]:
            if distance[i[1]] > cost + i[0]:
                distance[i[1]] = cost + i[0]
                heapq.heappush(q, (i[0]+cost, i[1]))
    return distance[1:]

distance_a = dijkstra(1)
b = 0
b_dist = 0
for node, dist in enumerate(distance_a, start=1):
    if b_dist < dist:
        b = node
        b_dist = dist
print(max(dijkstra(b)))