import sys
N, M = map(int, sys.stdin.readline().split())
sum_set = set()
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
block_set = [
    ((0,1),(0,2),(0,3)),
    ((1,0),(2,0),(3,0)),
    ((0,1),(0,2),(-1,2)),
    ((0,1),(0,2),(1,2)),
    ((1,0),(2,0),(2,1)),
    ((1,0),(2,0),(2,-1)),
    ((1,0),(2,0),(0,-1)),
    ((1,0),(2,0),(0,1)),
    ((0,1),(0,2),(1,0)),
    ((0,1),(0,2),(-1,0)),
    ((1,0),(1,1),(2,1)),
    ((0,1),(-1,1),(-1,2)),
    ((1,0),(1,-1),(2,-1)),
    ((0,1),(1,1),(1,2)),
    ((0,1),(1,0),(1,1)),
    ((1,0),(2,0),(1,1)),
    ((1,0),(2,0),(1,-1)),
    ((0,1),(0,2),(-1,1)),
    ((0,1),(0,2),(1,1)),
]

for i in range(N):
    for j in range(M):
        for shape in block_set:
            tmp = board[i][j]
            for x, y in shape:
                if not (0<=i+x<N) or not (0<=j+y<M):
                    break
                tmp += board[i+x][j+y]
            else:
                sum_set.add(tmp)

print(max(sum_set))

# -------------------------------------------------------------------------

import sys
N, M = map(int, sys.stdin.readline().split())
result = 0
board = []
visited = [[0]*M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

MAX = max(map(max, board))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(cnt:int, x:int, y:int, total:int):
    global result
    visited[x][y] = 1
    if result >= total + MAX * (3-cnt):
        return
    if cnt == 3:
        result = max(result, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] != 1:
            if cnt == 1:
                visited[nx][ny] = 1
                dfs(cnt+1, x, y, total+board[nx][ny])
                visited[nx][ny] = 0

            visited[nx][ny] = 1
            dfs(cnt+1, nx, ny, total+board[nx][ny])
            visited[nx][ny] = 0
    return

for i in range(N):
    for j in range(M):
        dfs(0, i, j, board[i][j])
        visited[i][j] = 0

print(result)