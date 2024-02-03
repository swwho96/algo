import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
dp = [[0 for j in range(202)] for i in range(202)]

for i in range(202):
    for j in range(0, i+1):
        if i==0 or j==0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            if dp[i][j] > 1000000000:
                dp[i][j] = 1000000001

if dp[i+j][j] < K:
    print(-1)
else:
    while not (N==0 and M==0):
        if dp[N-1+M][M] >= K:
            print('a', end='')
            N -= 1
        else:
            print('z', end='')
            K -= dp[N-1+M][M]
            M -= 1