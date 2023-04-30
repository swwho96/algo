'''
인접한 칸 - 상하좌우

비어있는 모든 칸을 확인하면서,
해당 자리 인접한 곳에 앉은 좋아하는 학생 수를 세고,
인접한 자리가 비어있는 칸의 수를 세어,
(좋아하는 학생 수, 빈칸, r행, c열)로 q에 담는다.

q를 -x[0], -x[1], x[2], x[3]로 정렬하고 가장 첫 자리에 앉는다. => heapq로 해결

모든 학생이 자리에 앉으면 만족도 조사를 실시한다.
0인 경우 0, else 10 ** (인접한 좋아하는 학생 수 - 1)
'''

import sys
import heapq
input = sys.stdin.readline
n = int(input())
board = [[0] * n for _ in range(n)]
student = {}
for _ in range(n**2):
    tmp = list(map(int, input().split()))
    student[tmp[0]] = tmp[1:]

# 학생 자리 배치
for s, lover in student.items():
    h = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                tmp = 0
                empty_cnt = 0
                for a, b in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i+a, j+b
                    if 0<=ni<n and 0<=nj<n:
                        if board[ni][nj] in lover:
                            tmp += 1
                        elif board[ni][nj] == 0:
                            empty_cnt += 1
                heapq.heappush(h, (-tmp, -empty_cnt, i, j))
    _, _, x, y = heapq.heappop(h)
    board[x][y] = s

# 만족도 조사
satisfaction = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for a, b in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=i+a<n and 0<=j+b<n and board[i+a][j+b] in student[board[i][j]]:
                cnt += 1
        satisfaction += 10 ** (cnt-1) if cnt > 0 else 0

print(satisfaction)