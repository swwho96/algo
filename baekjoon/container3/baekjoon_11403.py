import sys
input = sys.stdin.readline
board = []
n = int(input())
for _ in range(n):
    board.append(list(map(int, input().split())))

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][k] > 0 and board[k][j] > 0:
                board[i][j] = 1

# 출력
for i in range(n):
    print(*board[i])