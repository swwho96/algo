import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a,b,parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b, parent)
    elif op == 1:
        print('NO' if find(a,parent) != find(b,parent) else 'YES')