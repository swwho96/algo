import sys
input = sys.stdin.readline
N = int(input().rstrip())
forest = []
dp = [[-1] * N for _ in range(N)]
for _ in range(N):
    forest.append(list(map(int, input().split())))

# DFS후 각 위치에 몇칸을 갈 수 있는지 적는다
# 만약 해당 위치의 DP가 0이라면 새로 기록한다

def dfs(x:int, y:int):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for nr, nc in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=nr<N and 0<=nc<N and forest[nr][nc] > forest[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nr,nc)+1)
    return dp[x][y]

result = 0
for i in range(N):
    for j in range(N):
        dp[i][j] = dfs(i,j)

print(result)