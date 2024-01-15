from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (N+1)
distance = [int(10e9)] * (N+1)
distance[X] = 0
visited[X] = True
def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] is False and distance[i] > distance[now] + 1:
                distance[i] = distance[now] + 1
                visited[i] = True
                q.append(i)

bfs(X)

cnt = 0
for idx in range(1, N+1):
    if distance[idx] == K:
        cnt += 1
        print(idx)

if cnt == 0:
    print(-1)