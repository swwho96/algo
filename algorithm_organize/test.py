# 음료수 얼려 먹기 - bfs
from queue import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

icecream = 0

def bfs(graph, x, y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for a, b in zip([-1,1,0,0], [0,0,-1,1]):
            nx = x + a
            ny = y + b
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == '0':
                    q.append((nx, ny))
                    graph[nx][ny] = '#'

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            bfs(graph, i, j)
            icecream += 1

print(icecream)