import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = [(0,0)]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx,ny))
    return board[-1][-1]

print(bfs())