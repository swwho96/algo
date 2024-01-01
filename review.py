import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 배열 담기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 질의 담기
queries = []
for _ in range(M):
    queries.append(list(map(int, input().split())))

# 구간합 구하기
S = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + board[i-1][j-1]

for q in queries:
    x1, y1, x2, y2 = q
    answer = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(answer)