import sys
from collections import deque
N = int(sys.stdin.readline())
board = []
help_time = 0
shark = 2
eat = 0
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# 물고기 위치 파악
fish_cnt = 0
fish_area = []
for i in range(N):
    for j in range(N):
        if 1<=board[i][j]<=6:
            fish_cnt += 1
            fish_area.append((i,j))
        elif board[i][j] == 9:
            r, c = i, j

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(r,c,shark):
    q = deque([(r,c)])
    dist = [[0] * N for _ in range(N)]
    prey = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and dist[nx][ny] == 0 and board[nx][ny] <= shark:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                if 0< board[nx][ny] <shark:
                    prey.append((dist[nx][ny], nx, ny))
    if prey:
        return sorted(prey, key=lambda x: (x[0], x[1], x[2]))
    else:
        return None

while fish_cnt > 0:
    board[r][c] = 0
    a = bfs(r, c, shark)
    if a is None:
        break
    dist, r, c = a.pop(0)
    help_time += dist
    fish_cnt -= 1
    eat += 1
    if eat == shark:
        shark += 1
        eat = 0

print(help_time)