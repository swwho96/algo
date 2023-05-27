import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))
dice = [[4,1,3], [2,1,5,6]]
result = 0


def bfs(q, B):
    global result
    v = [[False] * M for _ in range(N)]
    cnt = 1
    while q:
        x, y = q.popleft()
        v[x][y] = True
        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+i, y+j
            if 0<=nx<N and 0<=ny<M and v[nx][ny] is False and maps[nx][ny] == B:
                cnt += 1
                v[nx][ny] = True
                q.append((nx,ny))
    result += B * cnt
    

def dice_rotate(d):
    global dice
    if d == 0:
        dice[0] = [dice[1][-1]] + dice[0]
        dice[1][-1] = dice[0][-1]
        dice[0] = dice[0][:3]
        dice[1][1] = dice[0][1]
    if d == 1:
        dice[1] = [dice[1][-1]] + dice[1][:3]
        dice[0][1] = dice[1][1]
    if d == 2:
        dice[0] = dice[0] + [dice[1][-1]]
        dice[1][-1] = dice[0][0]
        dice[0] = dice[0][1:]
        dice[1][1] = dice[0][1]
    if d == 3:
        dice[1] = dice[1][1:] + [dice[1][0]]
        dice[0][1] = dice[1][1]


x, y, d = 0, 0, 0
move = [(0,1),(1,0),(0,-1),(-1,0)]
d_change = {0:2, 1:3, 2:0, 3:1}
for c in range(K):
    if 0<=x + move[d][0]<N and 0<=y + move[d][1]<M:
        x, y = x + move[d][0], y + move[d][1]
    else:
        d = d_change[d]
        x, y = x + move[d][0], y + move[d][1]
    dice_rotate(d)
    Q = deque([(x,y)])
    bfs(Q, maps[x][y])
    if dice[1][-1] > maps[x][y]:
        d = (d+1) % 4
    elif dice[1][-1] < maps[x][y]:
        d = d-1 if d >= 1 else 3

print(result)