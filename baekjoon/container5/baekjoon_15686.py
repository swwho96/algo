import sys
from itertools import combinations
input = sys.stdin.readline

# 입력받기
board = []
n, m = map(int, input().split())
for _ in range(n):
    board.append(list(map(int, input().split())))

# 치킨집, 집 좌표 구하기
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i, j))
        elif board[i][j] == 1:
            home.append((i, j))

# 치킨집 M개 고르기
chicken = combinations(chicken, min(m, len(chicken)))

# 조합 별 치킨거리 구하기
city_chicken_dist = int(1e9)
for combi in chicken:
    dist_by_combi = 0
    for hx, hy in home:
        tmp = int(1e9)
        for cx, cy in combi: # 집과 가장 가까운 치킨집 찾기
            tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        dist_by_combi += tmp
    city_chicken_dist = min(city_chicken_dist, dist_by_combi)
print(city_chicken_dist)