import sys
input = sys.stdin.readline

T = int(input())
board = [[0] * 31 for _ in range(31)]
for i in range(31):
    board[i][1] = i # 1개만 선택하는 경우
    board[i][0] = 1 # 1개도 선택하지 않는 경우
    board[i][i] = 1 # 전부 선택하는 경우

for i in range(1, 31):
    for j in range(1, 31):
        board[i][j] = board[i-1][j-1] + board[i-1][j]

for _ in range(T):
    N, M = map(int, input().split())
    print(board[M][N])