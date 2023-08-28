n, m, k = map(int, input().split())
dp = [[0 for _ in range(202)] for _ in range(202)]
for i in range(201):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            if dp[i][j] > 1000000000:
                dp[i][j] = 1000000001

if dp[n+m][m] < k:
    print(-1)
else:
    while not (n==0 and m==0):
        if dp[n-1+m][m] >= k:
            print('a', end='')
            n -= 1
        else:
            print('z', end='')
            k -= dp[n-1+m][m]
            m -= 1