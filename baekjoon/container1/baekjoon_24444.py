import sys
from collections import deque
N, M, R = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([R])
visited = [False for _ in range(N+1)]
time, visit_time = 1, [0 for _ in range(N+1)]
while q:
    now = q.popleft()
    if visited[now] is False:
        visited[now] = True
        visit_time[now] = time
        time += 1
        for i in sorted(graph[now]):
            if visited[i] is False:
                q.append(i)

for i in range(1, N+1):
    print(visit_time[i])