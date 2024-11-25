# 최소 연산 횟수 구하기
# 현재 들어온 행렬을 확인하는 방법
import sys
input = sys.stdin.readline

N = int(input().rstrip())
mats = []
for _ in range(N):
    mats.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

for interval in range(1, N):
    for s in range(N-interval):
        e = s + interval
        if interval == 1:
            dp[s][e] = mats[s][0]*mats[s][1]*mats[e][1]
            continue
        dp[s][e] = float('inf')
        for k in range(s, e):
            dp[s][e] = min(dp[s][e], dp[s][k]+dp[k+1][e]+mats[s][0]*mats[k][1]*mats[e][1])

print(dp[0][-1])