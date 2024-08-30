import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    I = int(input().rstrip())
    now_x, now_y = map(int, input().split())
    to_x, to_y = map(int, input().split())
    board = [[float('inf')] * I for _ in range(I)]
    board[now_x][now_y] = 0
    q = deque([(now_x, now_y)])
    flag = True
    while q and flag:
        nx, ny = q.popleft()
        for i, j in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
            if 0<=nx+i<I and 0<=ny+j<I and board[nx+i][ny+j] == float('inf') and board[nx+i][ny+j] > board[nx][ny] + 1:
                board[nx+i][ny+j] = board[nx][ny] + 1
                if nx+i == to_x and ny+j == to_y:
                    flag = False
                    break
                q.append((nx+i,ny+j))
    print(board[to_x][to_y])