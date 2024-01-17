import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
build_time = [0] * (N+1)
result = [0] * (N+1)
for i in range(1, N+1):
    infos = list(map(int, input().split()))[:-1]
    result[i] = infos[0]
    for bilding in infos[1:]:
        graph[bilding].append(i)
        indegree[i] += 1

q = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        build_time[i] = max(build_time[i], result[now])
        indegree[i] -= 1
        if indegree[i] == 0:
            result[i] += build_time[i]
            q.append(i)

for i in range(1, N+1):
    print(result[i])