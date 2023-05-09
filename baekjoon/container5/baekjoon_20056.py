import sys
from collections import defaultdict
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = defaultdict(list)
direct = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}
# 파이어볼 배치
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    board[(r,c)].append((m,s,d))

# 이동 명령
for _ in range(K):
    move_board = defaultdict(list)
    sum_board = defaultdict(list)
    # 이동
    for k, v in board.items():
        r, c = k[0], k[1]
        for m,s,d in v:
            move_board[(((r+s*direct[d][0])%N),(c+s*direct[d][1])%N)].append((m,s,d))
    # 분배
    for k, v in move_board.items():
        r,c = k[0], k[1]
        if len(v) <= 1:
            continue
        tmp_m, tmp_s, tmp_d, tmp_v = 0, 0, set(), []
        # 파이어볼 합체
        for m,s,d in v:
            tmp_m += m
            tmp_s += s
            tmp_d.add(d % 2)
        if tmp_d == set([1]) or tmp_d == set([0]):
            tmp_v = [(tmp_m//5, tmp_s//len(v), i) for i in [0,2,4,6]]
        else:
            tmp_v = [(tmp_m//5, tmp_s//len(v), i) for i in [1,3,5,7]]
        # 질량 0인 공 삭제
        tmp = []
        for a in tmp_v:
            if a[0] != 0:
                tmp.append(a)
        move_board[(r,c)] = tmp
    board = move_board

# 질량 합 계산
total_m = 0
for k, v in board.items():
    for m,s,d in v:
        total_m += m
print(total_m)