import sys
import copy
from collections import deque
input = sys.stdin.readline
n, m, h = map(int, input().split())
graph = [[0]*(h+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b][a] = 1

need_bridge = int(1e9) # 결과

# 사다리 놓을 수 있는 경우 찾기
q = []
for i in range(1,n):
    for j in range(1,h+1):
        if graph[i][j] == 0 and graph[i+1][j] == 0 and graph[i-1][j] == 0:
            q.append((i, j))

# i번이 i번에 도착하는지 확인
def check(g):
    for i in range(1,n+1):
        idx = i
        for j in range(1, h+1):
            if g[idx][j] == 1:
                idx += 1
            elif g[idx-1][j] == 1:
                idx -= 1
        if idx !=  i:
            return False
    return True


# 사다리를 하나씩 추가해가며 되는 경우 확인
def bfs(q, cnt):
    global need_bridge
    if not q or cnt > need_bridge or cnt > 3:
        return
    if check(graph):
        need_bridge = min(need_bridge, cnt)
        return
    for i, (col, row) in enumerate(q):
        if graph[col-1][row] == 0 and graph[col+1][row] == 0:
            graph[col][row] = 1 
            bfs(q[i+1:], cnt+1)
            graph[col][row] = 0

bfs(q, 0)
print(-1 if need_bridge > 3 else need_bridge)