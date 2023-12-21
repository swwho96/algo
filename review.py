import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

for _ in range(m):
    q, x, y = map(int, input().split())
    if q == 0:
        union(x, y)
    elif q == 1:
        print('NO') if find(x) != find(y) else print('YES')