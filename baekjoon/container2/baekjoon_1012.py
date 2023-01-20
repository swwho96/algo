import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1, 1]
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추밭 생성
    graph = [[0] * M for _ in range(N)]
    # 배추밭 배추 심기
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
    # bfs정의
    def bfs(x, y):
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
    # 배추흰지렁이 풀기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)