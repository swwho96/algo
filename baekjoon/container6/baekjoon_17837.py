import sys
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
tockens = defaultdict(list)
tocken_map = defaultdict(list)
for i in range(1,K+1):
    r,c,d = map(int, input().split())
    tockens[i] = [r-1,c-1,d]
    tocken_map[(r-1,c-1)].append(i)


to_move = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
move_change = [-1, 2, 1, 4, 3]
turn = 0
game = True
while turn < 1000:
    turn += 1
    for i in range(1, K+1):
        r, c, d = tockens[i]
        idx = tocken_map[(r,c)].index(i)
        nr, nc = r + to_move[d][0], c + to_move[d][1]
        # 이동하려는 칸이 파란색인 경우 2
        if not (0<=nr<N and 0<=nc<N) or board[nr][nc] == 2:
            nr, nc = r - to_move[d][0], c - to_move[d][1]
            d = move_change[d]
            if not (0<=nr<N and 0<=nc<N) or board[nr][nc] == 2:
                tockens[i] = [r, c, d]
                continue
        # 이동하려는 칸이 흰색인 경우 0
        if board[nr][nc] == 0 and 0<=nr<N and 0<=nc<N:
            tocken_map[(nr,nc)] += tocken_map[(r,c)][idx:]
            if len(tocken_map[(nr, nc)]) >= 4:
                game = False
                break
            for t in tocken_map[(r,c)][idx:]:
                tockens[t] = [nr, nc, tockens[t][2]]
            tocken_map[(r,c)] = tocken_map[(r,c)][:idx]
            tockens[i] = [nr, nc, d]
        # 이동하려는 칸이 빨간색인 경우 1
        elif board[nr][nc] == 1 and 0<=nr<N and 0<=nc<N:
            tocken_map[(nr,nc)] += reversed(tocken_map[(r,c)][idx:])
            if len(tocken_map[(nr, nc)]) >= 4:
                game = False
                break
            for t in reversed(tocken_map[(r,c)][idx:]):
                tockens[t] = [nr, nc, tockens[t][2]]
            tocken_map[(r,c)] = tocken_map[(r,c)][:idx]
            tockens[i] = [nr, nc, d]
    if game is False:
        break
print(turn if turn < 1000 else -1)