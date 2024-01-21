import sys
from heapq import heappush, heappop
input = sys.stdin.readline

alpha = "abcdefghijklmnopqrstuvwxyz"
len_dict = {}
for idx, char in enumerate(alpha, start=1):
    len_dict[char] = idx
    len_dict[char.upper()] = idx+26

N = int(input())
total_lenline = 0
graph = [[int(10e9)] * (N+1) for _ in range(N+1)]
tmp = []
for _ in range(N):
    tmp.append(list(input().rstrip()))

heap = []
for i in range(N):
    for j in range(N):
        if tmp[i][j].isalpha():
            graph[i][j] = len_dict[tmp[i][j]]
            total_lenline += len_dict[tmp[i][j]]
            heappush(heap, (len_dict[tmp[i][j]], i, j))

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    parent[max(a,b)] = min(a,b)

give_lenline = total_lenline
parent = [i for i in range(N)]
while heap:
    cost, a, b = heappop(heap)
    if find(a, parent) != find(b, parent):
        union(a, b, parent)
        give_lenline -= cost

for i in range(N):
    find(i, parent)

print(-1 if sum(parent) != 0 else give_lenline)