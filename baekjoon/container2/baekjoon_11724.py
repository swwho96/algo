import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    parent[max(a,b)] = min(a,b)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: min(x))

for e in edges:
    a, b = e
    if find_parent(a, parent) != find_parent(b, parent):
        union_parent(a,b,parent)

print(len(set(parent[1:])))