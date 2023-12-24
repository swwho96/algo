import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(10e9)
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1,N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()