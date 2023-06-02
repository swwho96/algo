import sys
import copy
from itertools import product
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def up_and_down(reverse=False, flip=False):
    global board_copy
    if flip is True:
        board_tmp = []
        for b in list(zip(*board_copy)):
            board_tmp.append(list(b))
        board_copy = board_tmp
    if reverse is True:
        board_copy.reverse()
    for i in range(N):
        tmp = []
        for row in board_copy:
            if row[i] != 0:
                tmp.append(row[i])
        tmp = tmp + [0] * (N-len(tmp))
        tmp_sum = []
        idx = 0
        while idx < N:
            if idx < N-1 and tmp[idx] == tmp[idx+1]:
                tmp_sum.append(tmp[idx]+tmp[idx+1])
                idx += 2
            else:
                tmp_sum.append(tmp[idx])
                idx += 1
        tmp_sum = tmp_sum + [0] * (N-len(tmp_sum))
        for idx, j in enumerate(tmp_sum):
            board_copy[idx][i] = j
    if reverse is True:
        board_copy.reverse()
    if flip is True:
        board_tmp = []
        for b in list(zip(*board_copy)):
            board_tmp.append(list(b))
        board_copy = board_tmp

result = 0
combi = product([0,1,2,3], repeat=5)
for c in combi:
    board_copy = copy.deepcopy(board)
    for d in c:
        if d == 0:
            up_and_down(False, False)
        elif d == 1:
            up_and_down(True, False)
        elif d == 2:
            up_and_down(False, True)
        elif d == 3:
            up_and_down(True, True)
    for row in board_copy:
        result = max(result, max(row))

print(result)