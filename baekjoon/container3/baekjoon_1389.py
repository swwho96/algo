import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 친구관계 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 케빈 베이컨 계산 (플로이드-워셜)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 케빈 베이컨이 가장 작은 사람
bacon = INF
result = 0
for i in range(1, n+1):
    tmp = sum(graph[i][1:])
    if bacon > tmp:
        bacon = tmp
        result = i

print(result)

# _____________________________________________________________________________

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
result_u = 0
result_bacon = INF

friends = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for u in range(1, n+1):
    bacon = {u:0}
    q = deque([u])
    while q:
        now = q.popleft()
        for next_u in friends[now]:
            if next_u not in bacon:
                bacon[next_u] = bacon[now]+1
                q.append(next_u)
    now_bacon = sum(bacon.values())
    if result_bacon > now_bacon:
        result_bacon = now_bacon
        result_u = u

print(result_u)