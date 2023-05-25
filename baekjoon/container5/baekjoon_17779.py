import sys
input = sys.stdin.readline
n = int(input())
board = [[0]* (n+1)]
total_population = 0
result = int(1e9)
for _ in range(n):
    tmp = [0] + list(map(int, input().split()))
    total_population += sum(tmp)
    board.append(tmp)

def solution(total, x, y, d1, d2):
    temp = [[0] * (n+1) for _ in range(n+1)]
    cnt_by_area = [0] * 5
    temp[x][y] = 5
    for i in range(d1+1):
        temp[x+i][y-i] = 5
    for i in range(d2+1):
        temp[x+i][y+i] = 5
    for i in range(d2+1):
        temp[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        temp[x+d2+i][y+d2-i] = 5

    for r in range(1, x+d1):
        for c in range(1, y+1):
            if temp[r][c] != 5:
                cnt_by_area[0] += board[r][c]

    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if temp[r][c] == 5:
                break
            else:
                cnt_by_area[1] += board[r][c]

    # for r in range(1, x + d2 + 1):
    #     for c in range(n, y, -1):
    #         if temp[r][c] == 5:
    #             break
    #         else:
    #             cnt_by_area[1] += board[r][c]

    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if temp[r][c] != 5:
                cnt_by_area[2] += board[r][c]

    for r in range(x+d2+1, n+1):
        for c in range(n, y-d1+d2-1, -1):
            if temp[r][c] != 5:
                cnt_by_area[3] += board[r][c]

    cnt_by_area[4] = total - sum(cnt_by_area)
    return max(cnt_by_area) - min(cnt_by_area)

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                # 1번 조건
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue
                result = min(result, solution(total_population, x, y, d1, d2))
print(result)