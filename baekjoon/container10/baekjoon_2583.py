import sys
from collections import deque
input = sys.stdin.readline

def fill_rect(x1:int, y1:int, x2:int, y2:int)->None:
    global board
    for c in range(x1, x2):
        for r in range(y1, y2):
            board[r][c] = 1
    return None

# def find_space(x:int, y:int)->int:
#     global board
#     cnt = 1
#     q = deque([(x,y)])
#     board[x][y] = -1
#     while q:
#         r, c = q.popleft()
#         for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
#             if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 0:
#                 board[nr][nc] = -1
#                 cnt += 1
#                 q.append((nr,nc))
#     return cnt
def find_space(x:int, y:int)->int:
    global board, tmp
    stack = [(x,y)]
    board[x][y] = -1
    while stack:
        r, c = stack.pop()
        for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 0:
                board[nr][nc] = -1
                tmp += 1
                find_space(nr, nc)


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    fill_rect(x1, y1, x2, y2)

result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            tmp = 1
            find_space(i, j)
            result.append(tmp)

result.sort()
print(len(result))
print(' '.join(map(str, result)))