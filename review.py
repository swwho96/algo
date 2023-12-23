import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# 그래프
indgree = [0] * (N+1)
costs = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    tmp = list(map(int, input().split()))
    tmp.pop()
    costs[i] = tmp[0]
    for building in tmp[1:]:
        graph[building].append(i)
        indgree[i] += 1

# 진입차수 0인 건물 짓기
q = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        q.append(i)

result = [0] * (N+1)
while q:
    now = q.popleft()
    for b in graph[now]:
        indgree[b] -= 1
        result[b] = max(result[b], result[now]+costs[now])
        if indgree[b] == 0:
            q.append(b)

for i in range(1, N+1):
    print(result[i]+costs[i])