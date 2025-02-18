N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[1][i] = 1

for k in range(2,K+1):
    for n in range(N+1):
        dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000

print(dp[N][K] % 1000000000)

# ------------------------------------------------------------
N, K = map(int, input().split())
a,b = 1,1

for i in range(1, K):
    a *= N + i
    b *= i

print((a // b) % 1000000000)