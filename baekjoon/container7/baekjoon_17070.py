import sys
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

result = 0
def pipemove(direct, x, y):
    global result, board
    if x == N-1 and y == N-1:
        result += 1
        return
    if direct == '-':
        # -
        nx, ny = x, y+1
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            pipemove('-', nx, ny)
        # \
        nx, ny = x+1, y+1
        if 0<=nx<N and 0<=ny<N and (board[nx][ny] == 0 and board[nx-1][ny] == 0 and board[nx][ny-1] == 0):
            pipemove('\\', nx, ny)
    elif direct == "\\":
        # -
        nx, ny = x, y+1
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            pipemove('-', nx, ny)
        # |
        nx, ny = x+1, y
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            pipemove('|', nx, ny)
        # \
        nx, ny = x+1, y+1
        if 0<=nx<N and 0<=ny<N and (board[nx][ny] == 0 and board[nx-1][ny] == 0 and board[nx][ny-1] == 0):
            pipemove('\\', nx, ny)
    elif direct == '|':
        # |
        nx, ny = x+1, y
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == 0:
            pipemove('|', nx, ny)
        # \
        nx, ny = x+1, y+1
        if 0<=nx<N and 0<=ny<N and (board[nx][ny] == 0 and board[nx-1][ny] == 0 and board[nx][ny-1] == 0):
            pipemove('\\', nx, ny)

pipemove('-', 0, 1)
print(result)