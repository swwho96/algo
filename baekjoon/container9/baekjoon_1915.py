import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

dp = [[0]*M for _ in range(N)]
for i in range(N):
    if i == 0:
        for j in range(M):
            dp[i][j] = board[i][j]
    else:
        dp[i][0] = board[i][0]

for d in dp:
    print(d)

answer = max(max(dp))
for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == 0:
            dp[i][j] = 0
        else:
            tmp = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            dp[i][j] = tmp + 1
            answer = max(answer, dp[i][j])
print(answer ** 2)