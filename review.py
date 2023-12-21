import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
indgree = [0] * (N+1)
costs = [0] * (N+1)

for i in range(1,N+1):
    building_info = list(map(int, input().split()))
    costs[i] = building_info[0]
    for b_num in building_info[1:-1]:
        graph[b_num].append(i)
        indgree[i] += 1

q = deque()

for i in range(1, N+1):
    if indgree[i] == 0:
        q.append(i)

result = [0] * (N+1)

while q:
    now = q.popleft()
    for i in graph[now]:
        indgree[i] -= 1
        result[i] = max(result[i], result[now]+costs[now])
        if indgree[i] == 0:
            q.append(i)

for i in range(1, N+1):
    print(result[i]+costs[i])