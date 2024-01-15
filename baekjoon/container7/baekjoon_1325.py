import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
computer = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    computer[b].append(a)

# bfs
def bfs(v):
    q = deque([v])
    visited[v] = True
    cnt = 0
    while q:
        now = q.popleft()
        for i in computer[now]:
            if visited[i] is False:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt

# 모든 컴퓨터 확인
result = []
for c in range(1, n+1):
    visited = [False] * (n+1)
    result.append(bfs(c))

# 가장 많은 값
maxResult = max(result)
for idx, i in enumerate(result, start=1):
    if i == maxResult:
        print(idx, end=' ')