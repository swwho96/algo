import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
delete_node = int(input())
graph = [[] for _ in range(N)]
for node, parent in enumerate(info):
    if parent != -1:
        graph[parent].append(node)
    else:
        start = node

visited = [0] * (N)
def bfs(start, delete, cnt):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        if len(graph[now]) == 0 or graph[now] == [delete_node]:
            cnt += 1
            continue
        for i in graph[now]:
            if i == delete:
                continue
            elif visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return cnt

if start == delete_node:
    print(0)
else:
    result = bfs(start, delete_node, 0)
    print(visited)
    print(result if result > 0 else 1)



#  0
# 1 2
#   4
#   5 6
#   3  7 8