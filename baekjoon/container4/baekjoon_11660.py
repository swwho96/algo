import sys
input = sys.stdin.readline
n, m = map(int,input().split())

table, op = [[0]*(n+1)], []
dp = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    table.append([0]+list(map(int, input().split())))
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    op.append((x1,y1,x2,y2))

for i in range(1,n+1):
    dp[i][1] = table[i][1]
    for j in range(2,n+1):
        dp[i][j] = dp[i][j-1] + table[i][j]

for i in range(2,n+1):
    for j in range(1, n+1):
        dp[i][j] += dp[i-1][j]

result = []
for x1,y1,x2,y2 in op:
    tmp = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1]
    result.append(tmp)
for r in result:
    print(r)