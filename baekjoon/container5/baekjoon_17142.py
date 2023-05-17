import sys 
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
min_time = int(1e9)
zero_cnt = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

q = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            q.append((i,j))
            # zero_cnt += 1
        elif board[i][j] == 0:
            zero_cnt += 1

def virus_spread(t: list, q)->int:
    global zero_cnt
    b = copy.deepcopy(t)
    visited = set()
    time = 0
    zero = 0
    q = deque(q)
    while q:
        virus = []
        while q:
            i, j = q.popleft()
            for r, c in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+r, j+c
                if 0<=ni<n and 0<=nj<n and (b[ni][nj] == 0 or b[ni][nj] == 2) and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    virus.append((ni, nj))
        tmp = []
        for x, y in virus:
            if b[x][y] == 0:
                tmp.append((x,y))
            b[x][y] = 9
        q += virus
        if virus or tmp: time += 1
        zero += len(tmp)
        if zero_cnt == zero:
            return time, zero
    return time, zero

for info in combinations(q, m):
    tmp_time, tmp_zero = virus_spread(board, info)
    if zero_cnt == 0:
        min_time = 0
    elif tmp_zero == zero_cnt:
        min_time = min(min_time, tmp_time)

print(min_time if min_time < int(1e9) else -1)