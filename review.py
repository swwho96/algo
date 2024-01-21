from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
heap = []
for _ in range(E):
    a, b, c = map(int, input().split())
    heappush(heap, (c, a, b))

total_cost = 0
while heap:
    cost, s, e = heappop(heap)
    if find(s, parent) != find(e, parent):
        union(s, e, parent)
        total_cost += cost

print(total_cost)