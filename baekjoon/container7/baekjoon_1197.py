import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
result = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, (c, a, b))

while edges:
    cost, start, end = heapq.heappop(edges)
    if find(start) != find(end):
        union(start, end)
        result += cost

print(result)