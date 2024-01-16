import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N,M = map(int, input().split())

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

parent = [i for i in range(N+1)]
for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 1:
        print('YES' if find(a, parent) == find(b, parent) else 'NO')
    else:
        union(a, b, parent)