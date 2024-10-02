import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[float('inf'), float('inf')] for _ in range(N+1)]

def dfs(cur: int, parent: int):
    dp[cur][0] = 0  # cur 노드가 얼리 어답터가 아닐 때
    dp[cur][1] = 1  # cur 노드가 얼리 어답터일 때
    
    for node in graph[cur]:
        if node == parent:
            continue  # 부모 노드를 다시 방문하지 않도록 처리
        
        dfs(node, cur)  # 자식 노드를 재귀적으로 탐색
        
        # 자식 노드의 결과를 현재 노드에 반영
        dp[cur][0] += dp[node][1]  # 현재 노드가 얼리 어답터가 아닌 경우, 자식은 무조건 얼리 어답터여야 함
        dp[cur][1] += min(dp[node][0], dp[node][1])  # 현재 노드가 얼리 어답터인 경우, 자식은 얼리 어답터일 수도 있고 아닐 수도 있음

dfs(1,-1)
print(min(dp[1][0],dp[1][1]))