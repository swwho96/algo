import sys
input = sys.stdin.readline

N, D = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(N)]
routes = sorted(routes, key=lambda x: (x[0], -x[1], x[2]))
cur, total_dist = 0, 0
dp = [float('inf')] * (D+1)
dp[0] = 0
for i in range(D+1):
    if i+1 <= D:
        dp[i+1] = min(dp[i]+1, dp[i+1])
    for s,e,d in routes:
        if i == s and e <= D:
            dp[e] = min(dp[e], dp[i]+d)
print(dp[-1])