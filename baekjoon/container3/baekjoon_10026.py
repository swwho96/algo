from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = []
weakness_board = []
color_number_dict = {'R':'1', 'G':'2', 'B':'3'}
for _ in range(N):
    tmp = input().rstrip()
    board.append(list(tmp))
    weakness_board.append(list(tmp.replace('G', 'R')))

def bfs(x, y, b):
    global color_number_dict
    n = len(b)
    c = b[x][y]
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for xi, yi in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+xi
            ny = y+yi
            if 0<=nx<n and 0<=ny<n and b[nx][ny] == c:
                b[nx][ny] = color_number_dict[c]
                q.append((nx, ny))
    return b

result, weakness_result = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] in color_number_dict:
            board = bfs(i,j,board)
            result += 1
        if weakness_board[i][j] in color_number_dict:
            weakness_board = bfs(i,j,weakness_board)
            weakness_result += 1
            
print(result, weakness_result)

# ------------------------------------------------------------------------

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = []
weakness_board = []
visitied = [[0] * N for _ in range(N)]
weakness_visitied = [[0] * N for _ in range(N)]
for _ in range(N):
    tmp = input().rstrip()
    board.append(list(tmp))
    weakness_board.append(list(tmp.replace('G', 'R')))

def bfs(x, y, b, v):
    n = len(b)
    c = b[x][y]
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for xi, yi in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+xi
            ny = y+yi
            if 0<=nx<n and 0<=ny<n and not v[nx][ny] and b[nx][ny] == c:
                v[nx][ny] = 1
                q.append((nx, ny))
    return b, v

result, weakness_result = 0, 0
for i in range(N):
    for j in range(N):
        if not visitied[i][j]:
            board, visitied = bfs(i,j,board, visitied)
            result += 1
        if not weakness_visitied[i][j]:
            weakness_board, weakness_visitied = bfs(i,j,weakness_board, weakness_visitied)
            weakness_result += 1
            
print(result, weakness_result)


# --------------------------------------------------------------------
import sys
input = sys.stdin.readline
N = int(input())
board1 = []
board2 = []
for _ in range(N):
    tmp = input().rstrip()
    board1.append(list(tmp))
    board2.append(list(tmp.replace('R','A').replace('G','A')))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,b,color):
    b[x][y] = '#'
    stack = [(x,y)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<N and 0<=nc<N and b[nr][nc] == color:
                b[nr][nc] = '#'
                stack.append((nr,nc))

cnt1, cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if board1[i][j] != '#':
            dfs(i,j,board1,board1[i][j])
            cnt1 += 1
        if board2[i][j] != '#':
            dfs(i,j,board2,board2[i][j])
            cnt2 += 1

print(cnt1, cnt2)