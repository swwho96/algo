import sys
input = sys.stdin.readline
n, l = map(int, input().split())
board = []
way_cnt = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

# 행
answer = []
for b in (board+list(zip(*board))):
    idx = 0
    flag = True
    hill = False
    last = 0
    while True:
        if idx >= n-1:
            break
        idx += 1
        # 높이 차이가 2이상인 경우 불가능한 길
        if abs(b[idx] - b[idx-1]) > 1:
            flag = False
            break
        # 내리막 경사로
        if b[idx] - b[idx-1] == -1:
            for j in range(idx, idx+l):
                if b[idx] != b[j] or idx+l-1 > n-1:
                    flag = False
                    break
            else:
                idx = idx + l - 1
                last = idx
                hill = True
        # 오르막 경사로
        if b[idx] - b[idx-1] == 1:
            for j in range(idx-l, idx):
                if j < 0 or b[idx-1] != b[j] or (hill is True and j == last):
                    flag = False
                    break
            else:
                last = idx-l
                hill = True
        # 경사로를 놓을 수 없는 경우 불가능한 길
        if flag is False:
            break
    # 문제없이 지나왔다면 가능한 길
    if flag is True:
        way_cnt += 1
        answer.append(b)

print(way_cnt)