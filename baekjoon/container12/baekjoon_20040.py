import sys
input = sys.stdin.readline

N, M = map(int, input().split())

roots = [i for i in range(N)]

def find_root(x):
    if x != roots[x]:
        roots[x] = find_root(roots[x])
    return roots[x]

def union(a, b, roots):
    a = find_root(a)
    b = find_root(b)
    roots[max(a,b)] = min(a,b)

result = 0
for i in range(1, M+1):
    x, y = map(int, input().split())
    if find_root(x) == find_root(y) and result == 0: result = i
    union(x,y,roots)
print(result)