from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
q = deque([(0,0)])
while q:
    x, y = q.popleft()
    for i, j in zip([-1,1,0,0], [0,0,-1,1]):
        nx, ny = x+i, y+j
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph)