import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
dp = [0] * (n+1)
cost = [0] * (n+1)
indegree = [0] * (n+1)
for i in range(1, n+1):
    info = list(map(int, input().split()))
    cost[i] = info[0]
    indegree[i] = info[1]
    for j in range(info[1]):
        graph[info[2:][j]].append(i)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = cost[i]
while q:
    now = q.popleft()
    for i in graph[now]:
        dp[i] = max(dp[i], dp[now]+cost[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
print(max(dp))