import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
computer = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    computer[a].append(b)

result = [0] * (n+1)

# bfs
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        for i in computer[now]:
            if visited[i] is False:
                visited[i] = True
                result[i] += 1
                q.append(i)

# 모든 컴퓨터 확인
for c in range(1, n+1):
    visited = [False] * (n+1)
    bfs(c)

# 가장 많은 값
maxResult = max(result)
for idx, i in enumerate(result):
    if i == maxResult:
        print(idx, end=' ')