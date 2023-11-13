import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 각 섬의 경계 찾기
def find_boundary(x, y)->list:
    q = deque([(x,y)])
    boundaries = set()
    board[x][y] = 2
    while q:
        r, c = q.popleft()
        check = 0
        board[r][c] = 0
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+i, c+j
            if 0<=nr<N and 0<=nc<N and board[nr][nc] == 1:
                board[nr][nc] = 2
                q.append((nr, nc))
        boundaries.add((r, c))
    return boundaries

# 두 섬을 연결하는 다리의 최소 길이 구하기
def make_bridge(a:list, b:list)->int:
    global shortest_bridge
    for r1, c1 in a:
        for r2, c2 in b:
            shortest_bridge = min(shortest_bridge, abs(r1-r2)+abs(c1-c2)-1)
            if shortest_bridge == 1:
                return 


# 각 섬 별 경계선 찾기
island_boundaries = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            island_boundaries.append(find_boundary(i, j))

# 최소 길이 다리
shortest_bridge = int(10e9)
for i in range(len(island_boundaries)):
    for j in range(i+1, len(island_boundaries)):
        make_bridge(island_boundaries[i], island_boundaries[j])
        if shortest_bridge == 1:
            break
    if shortest_bridge == 1:
        break

print(shortest_bridge)