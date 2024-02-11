import sys
input = sys.stdin.readline

N = int(input())
days = [0] * (N+1)
costs = [0] * (N+1)
for i in range(1, N+1):
    info = list(map(int, input().split()))
    days[i] = info[0]
    costs[i] = info[1]

dp = [0] * (N+2)
for i in range(N, 0, -1):
    if i+days[i] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+days[i]]+costs[i])

print(dp[1])