import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

def check(num: int):
    return math.isqrt(num) ** 2 == num

answer = set()
for row_k in range(N+1):
    for col_k in range(M+1):
        if row_k == 0 and col_k == 0:
            continue
        for i in range(N):
            for j in range(M):
                for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    tmp_num = []
                    start_i, start_j = i, j
                    while 0 <= start_i < N and 0 <= start_j < M:
                        tmp_num.append(board[start_i][start_j])
                        num = int(''.join(tmp_num))
                        if check(num):
                            answer.add(num)
                        start_i += dr * row_k
                        start_j += dc * col_k

print(max(answer, default=-1))