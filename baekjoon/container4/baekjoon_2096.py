import sys
input = sys.stdin.readline
n = int(input())
board = []
for p in range(n):
    board = list(map(int, input().split()))
    if p == 0:
        dp_max, dp_min = board, board
    else:
        dp_max = [board[0] + max(dp_max[0], dp_max[1]), board[1] + max(dp_max), board[2] + max(dp_max[1], dp_max[2])]
        dp_min = [board[0] + min(dp_min[0], dp_min[1]), board[1] + min(dp_min), board[2] + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))