from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
board = []
weakness_board = []
color_number_dict = {'R':'1', 'G':'2', 'B':'3'}
for _ in range(N):
    tmp = input().rstrip()
    board.append(list(tmp))
    weakness_board.append(list(tmp.replace('G', 'R')))

def bfs(x, y, b):
    global color_number_dict
    n = len(b)
    c = b[x][y]
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for xi, yi in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+xi
            ny = y+yi
            if 0<=nx<n and 0<=ny<n and b[nx][ny] == c:
                b[nx][ny] = color_number_dict[c]
                q.append((nx, ny))
    return b

result, weakness_result = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] in color_number_dict:
            board = bfs(i,j,board)
            result += 1
        if weakness_board[i][j] in color_number_dict:
            weakness_board = bfs(i,j,weakness_board)
            weakness_result += 1
            
print(result, weakness_result)