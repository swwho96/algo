import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
lines = []
for _ in range(M):
    a,b,c = map(int, input().split())
    heapq.heappush(lines, (c,a,b))

def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(a,b,parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    parent[max(a,b)] = min(a,b)

total_cost = 0
parent = [i for i in range(N+1)]
while lines:
    cost, a, b = heapq.heappop(lines)
    if find_parent(a,parent) != find_parent(b,parent):
        union(a,b,parent)
        total_cost += cost
        
print(total_cost)