from collections import deque
import sys
input = sys.stdin.readline

def check(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
    return True

def bfs(board, q, tomato):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    new_q = []
    while q:
        x, y = q.popleft()
        board[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == 0:
                board[nx][ny] = 1
                tomato -= 1
                new_q.append((nx,ny))
    return board, new_q, tomato

n, m = map(int, input().split())
board = []
tomato = 0
for _ in range(m):
    board.append(list(map(int, input().split())))

# 초기 익은 토마토 위치
q = deque([])
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i,j))
        elif board[i][j] == 0:
            tomato += 1

# 토마토가 모두 익은 경우 0일 소요
if tomato == 0:
    print(0)
else: # 토마토 익히기
    days = 0
    while q:
        if tomato == 0:
            break
        days += 1
        board, new_q, tomato = bfs(board, q, tomato)
        q = deque(new_q)
    if tomato > 0: # 모든 토마토를 익히는게 불가능한 경우
        print(-1)
    else:
        print(days)