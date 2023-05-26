import sys
from collections import deque
input = sys.stdin.readline
N, Q = map(int, input().split())
maps = []
N = 2**N
for _ in range(N):
    maps.append(list(map(int, input().split())))
L = list(map(int, input().split()))

def rotate(l):
    for sx in range(0, N, l):
        for sy in range(0, N, l):
            origin = []
            for i in range(sx, sx+l):
                origin.append(maps[i][sy:sy+l])
            rotated = []
            for o in list(zip(*origin)):
                rotated.append(list(reversed(o)))
            for r in range(len(origin)):
                for c in range(len(origin[0])):
                    maps[sx+r][sy+c] = rotated[r][c]

def ice_check():
    global maps
    new_maps = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            flag = 0
            for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0<=i+a<N and 0<=j+b<N:
                    if maps[i+a][j+b] > 0:
                        flag += 1
            if flag >= 3:
                new_maps[i][j] = maps[i][j]
            else:
                if maps[i][j] > 0:
                    new_maps[i][j] = maps[i][j] - 1
    maps = new_maps

def final_ice_check():
    global maps
    result1, result2 = 0, 0
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result1 += maps[i][j]
            tmp_cnt = 0
            if maps[i][j] > 0 and v[i][j] is False:
                v[i][j] = True
                tmp_cnt += 1
                q = deque([(i, j)])
                while q:
                    tmp = []
                    while q:
                        x, y = q.popleft()
                        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if 0<=x+a<N and 0<=y+b<N and v[x+a][y+b] is False and maps[x+a][y+b] > 0:
                                v[x+a][y+b] = True
                                tmp_cnt += 1
                                tmp.append((x+a, y+b))
                    q = deque(tmp)
            result2 = max(result2, tmp_cnt)
    return result1, result2




for l in L:
    l = 2**l
    rotate(l)
    ice_check()
result1, result2 = final_ice_check()
print(result1)
print(result2)