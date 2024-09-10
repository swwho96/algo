import sys
from collections import deque
input = sys.stdin.readline

# 미로 입력
M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

# 미로의 각 위치 도달에 필요한 벽뚫기 횟수
min_crash_board = [[float('inf')] * M for _ in range(N)]
min_crash_board[0][0] = 0
q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+i, c+j
        if 0<=nr<N and 0<=nc<M and min_crash_board[r][c] + board[nr][nc] < min_crash_board[nr][nc]:
            min_crash_board[nr][nc] = min_crash_board[r][c] + board[nr][nc]
            if board[nr][nc] == 0: q.appendleft((nr,nc))
            else: q.append((nr,nc))
print(min_crash_board[-1][-1])