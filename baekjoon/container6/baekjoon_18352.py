import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
# 방향 그래프 정의
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
# 방문 처리
visited = [-1] * (n+1)
q = deque([x])
visited[x] = 0
while q:
    now = q.popleft()
    for i in city[now]:
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            q.append(i)
# k인 도시 찾기
flag = False
for idx, v in enumerate(visited):
    if v == k:
        flag = True
        print(idx)
if flag is False:
    print(-1)