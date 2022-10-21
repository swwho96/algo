import sys

N = int(sys.stdin.readline().rstrip())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[False for _ in range(N)] for _ in range(N)]
houses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            stack = [(i, j)]
            home_cnt = 0
            while stack:
                x, y = stack.pop()
                graph[x][y] = 9
                if visited[x][y] is False:
                    home_cnt += 1
                    visited[x][y] = True
                    for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                            if visited[nx][ny] is False:
                                stack.append((nx, ny))
            houses.append(home_cnt)

print(len(houses))
for i in sorted(houses):
    print(i)