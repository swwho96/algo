import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (V+1)
    def bfs(start):
        q = deque([start])
        visited[start] = 1
        while q:
            now = q.popleft()
            for i in graph[now]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = -1 * visited[now]
                elif visited[i] == visited[now]:
                    return False
        return True
    for v in range(1, V+1):
        if visited[v] == 0:
            result = bfs(v)
            if result is False:
                break
            
    print('YES' if result is True else 'NO')