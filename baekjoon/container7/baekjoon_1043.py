import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

truth = list(map(int, input().split()))
truth = truth[1:]
result = 0

P = []
for _ in range(m):
    party = list(map(int, input().split()))
    party = party[1:]
    P.append(party)
    for i in range(len(party)):
        for j in range(len(party)):
            union(party[i], party[j])

for p in P:
    flag = True
    for t in truth:
        if find(p[0]) == find(t):
            flag = False
            break
    result += 1 if flag is True else 0

print(result)