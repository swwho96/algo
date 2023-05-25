import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
maps = []
sand_out_of_map = 0
for _ in range(N):
    maps.append(list(map(int, input().split())))

def sand_spread(x, y, a, b, d):
    global sand_out_of_map
    spread_site = {
        0: [(-1,0),(1,0),(-1,-1),(1,-1),(-2,-1),(2,-1),(-1,-2),(1,-2),(0,-3)],
        1: [(0,-1),(0,1),(1,-1),(1,1),(1,-2),(1,2),(2,-1),(2,1),(3,0)],
        2: [(-1,0),(1,0),(-1,1),(1,1),(-2,1),(2,1),(-1,2),(1,2),(0,3)],
        3: [(0,-1),(0,1),(-1,-1),(-1,1),(-1,-2),(-1,2),(-2,-1),(-2,1),(-3,0)]
    }
    site_rate = [0.01,0.01,0.07,0.07,0.02,0.02,0.1,0.1,0.05]
    alpha_site = [(0,-2),(2,0),(0,2),(-2,0)]
    temp_sand = maps[a][b]

    for p, rate in zip(spread_site[d], site_rate):
        nx, ny = x + p[0], y + p[1]
        if 0<=nx<N and 0<=ny<N:
            maps[nx][ny] += int(temp_sand * rate)
        else:
            sand_out_of_map += int(temp_sand * rate)
        maps[a][b] -= int(temp_sand * rate)
    if 0<=x+alpha_site[d][0]<N and 0<=y+alpha_site[d][1]<N:
        maps[x+alpha_site[d][0]][y+alpha_site[d][1]] += maps[a][b]
    else:
        sand_out_of_map += maps[a][b]
    maps[a][b] = 0

def tornado(N):
    a = []
    Q = []
    for i in range(1, N):
        a += [i] * 2
    a.append(N-1)
    idx = 0
    for cnt in a:
        Q += ([idx] * cnt)
        idx = (idx + 1) % 4
    return deque(Q)

x, y = N // 2, N // 2
q = tornado(N)
direct = [(0,-1),(1,0),(0,1),(-1,0)]
while q:
    if x == 0 and y == 0:
        break
    d = q.popleft()
    a, b = x+direct[d][0], y+direct[d][1]
    sand_spread(x, y, a, b, d)
    x, y = a, b
    # for m in maps:
    #     print(m)
    # print()

print(sand_out_of_map)