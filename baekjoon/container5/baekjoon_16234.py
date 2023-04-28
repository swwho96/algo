import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,l,r = map(int, input().split())
board = []
day = 0
visitable = [[0] * n for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, input().split())))

def bfs(q, union, union_population):
    if not q:
        if union:
            for x, y in union:
                board[x][y] = union_population // len(union)
        return
    # 연합 국가 확인
    global visited, flag
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+i, y+j
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(board[x][y]-board[nx][ny])<=r:
                flag = True
                q.append((nx,ny))
                union.append((nx,ny))
                visited[nx][ny] = 1
                union_population += board[nx][ny]
        bfs(q, union, union_population)

# 하루 안에 일어나는 연합 과정
flag = True
while flag:
    visited = [[0]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(deque([(i,j)]), [(i,j)], board[i][j])
    if flag:
        day += 1
print(day)