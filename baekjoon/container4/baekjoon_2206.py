from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,w = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    q.append((nx,ny,w+1))
    return -1
    
print(bfs())