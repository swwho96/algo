import sys
from collections import Counter
input = sys.stdin.readline
r, c, k = map(int, input().split())
board = []
for _ in range(3):
    board.append(list(map(int, input().split())))

def list_sort(a:list)->list:
    a_cnt = Counter(a)
    if 0 in a_cnt:
        del a_cnt[0]
    tmp = []
    a_cnt = sorted(a_cnt.items(), key=lambda x: (x[1], x[0]))
    for k, v in a_cnt:
        tmp.append(k)
        tmp.append(v)
    return tmp


time = 0
while time < 100:
    if len(board) >= r and len(board[0]) >= c and board[r-1][c-1] == k:
        break
    time += 1
    list_length = 0
    # R연산
    if len(board) >= len(board[0]):
        for i in range(len(board)):
            board[i] = list_sort(board[i])
            list_length = max(list_length, len(board[i]))
        for i in range(len(board)):
            if len(board[i]) < list_length:
                board[i] += [0] * (list_length - len(board[i]))
                board[i] = board[i][:100]
    # C연산
    else:
        tmp_list = []
        tmp_board = []
        for b in list(zip(*board)):
            tmp = list_sort(b)
            tmp = tmp[:100]
            tmp_list.append(tmp)
            list_length = max(list_length, len(tmp))
        for i in range(len(tmp_list)):
            if len(tmp_list[i]) < list_length:
                tmp_list[i] += [0] * (list_length - len(tmp_list[i]))
        for t in zip(*tmp_list):
            tmp_board.append(list(t))
        board = tmp_board

print(time if time <= 100 else -1)