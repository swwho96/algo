import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

for i in range(1, n+1):
    info = list(map(int, input().split()))
    for j in range(n):
        if info[j] == 1 and find(i) != find(j+1):
            union(i, j+1)

plan = list(map(int, input().split()))
flag = set()
for p in plan:
    flag.add(parent[p])
print('YES' if len(flag) == 1 else 'NO')