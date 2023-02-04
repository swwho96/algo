from collections import deque
import sys
input = sys.stdin.readline
col, row, depth = map(int, input().split())
board = []
for _ in range(depth):
    tmp = []
    for _ in range(row):
        tmp.append(list(map(int, input().split())))
    board.append(tmp)

tomato = deque([])
for d in range(depth):
    for i in range(row):
        for j in range(col):
            if board[d][i][j] == 1:
                tomato.append((d, i, j))

dd = [0,0,0,0,-1,1]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]

def bfs(q):
    global board
    while q:
        d, x, y = q.popleft()
        for i in range(6):
            nd, nx, ny = d+dd[i], x+dx[i], y+dy[i]
            if 0<=nd<depth and 0<=nx<row and 0<=ny<col and board[nd][nx][ny] == 0:
                q.append((nd, nx, ny))
                board[nd][nx][ny] = board[d][x][y] + 1
    return

bfs(tomato)
result = 0
flag = True
for d in range(depth):
    for i in range(row):
        for j in range(col):
            if board[d][i][j] == 0:
                flag = False
            if result < board[d][i][j]:
                result = board[d][i][j]
if flag:
    print(result-1)
else:
    print(-1)