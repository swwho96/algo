'''공기청정기 위쪽은 반시계방향
공기청정기 아래는 시계방향
가장 바깥 (벽 주위)만 회전한다

미세먼지는 상하좌우로 각 방향 당 (1//5)만큼씩 확산'''

import sys
input = sys.stdin.readline
r,c,t = map(int, input().split())
board = []
air = []
for i in range(r):
    board.append(list(map(int, input().split())))
    if board[-1].count(-1) > 0:
        air.append(i)

# 행렬 테두리 회전
def up_rotate(b):
    tmp_up = b[0][0]
    b[0] = b[0][1:] + [b[1][-1]]
    tmp = b[-1][0]
    for i in range(len(b)-1, 0, -1):
        b[i][0] = b[i-1][0]
    b[1][0] = tmp_up
    tmp_down = b[-1][-1]
    b[-1] = [-1] + [0] + b[-1][1:-1]
    for i in range(1,len(b)):
        b[i-1][-1] = b[i][-1]
    b[-2][-1] = tmp_down
    return b

def down_rotate(b):
    tmp_up = b[0][-1]
    tmp_down = b[-1][-1]
    b[0] = [-1] + [0] + b[0][1:-1]
    for i in range(len(b)-1, 0, -1):
        b[i][-1] = b[i-1][-1]
    b[1][-1] = tmp_up
    tmp = b[-1][0]
    b[-1] = b[-1][1:-1] + [tmp_down] + [b[-1][-1]]
    for i in range(1,len(b)):
        b[i-1][0] = b[i][0]
    b[0][0] = -1
    b[-2][0] = tmp
    return b

for _ in range(t):
    # 미세먼지 확산
    q = []
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                q.append((board[i][j], i, j))
    for tmp, x, y in q:
        for a, b in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+a, y+b
            if 0<=nx<r and 0<=ny<c and board[nx][ny] >= 0:
                board[x][y] -= (tmp//5)
                board[nx][ny] += (tmp // 5)

    # 공기 순환
    a = up_rotate(board[:air[1]])
    b = down_rotate(board[air[1]:])
    board = a+b

# 미세먼지 양 확인
result = 2
for b in board:
    result += sum(b)

print(result)
