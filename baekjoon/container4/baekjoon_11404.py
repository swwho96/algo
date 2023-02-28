import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
board = [[int(1e9)] * (n) for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    board[a-1][b-1] = min(board[a-1][b-1], w)

for i in range(n):
    board[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])


for i in range(n):
    for j in range(n):
        if board[i][j] == int(1e9):
            print(0, end=' ')
        else: print(board[i][j], end=' ')
    print()