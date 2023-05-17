import sys
from collections import deque
input = sys.stdin.readline
A = []
N, M, K = map(int, input().split())
trees = [[deque([]) for _ in range(N)] for _ in range(N)]
board = [[5]*(N) for _ in range(N)]
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x,y,z = map(int, input().split())
    trees[x-1][y-1].append(z)

# K년 동안 반복
for p in range(K):
    # 봄 - 어린 나무부터 자신의 나이만큼 양분을 먹고, 나이가 1증가, 못먹으면 죽는다
    # 여름 - 봄에 죽은 나무가 양분으로 변환, 나이 // 2 가 해당 칸에 추가한다
    for i in range(N):
        for j in range(N):
            dead_tree = 0
            tmp = deque()
            while trees[i][j]:
                age = trees[i][j].pop()
                if board[i][j] - age < 0:
                    dead_tree += (age//2)
                else:
                    board[i][j] -= age
                    tmp.appendleft(age+1)
            trees[i][j] = deque(tmp)
            board[i][j] += dead_tree

    # 가을 - 5의 배수인 나이를 가진 나무는 상/하/좌/우/대각선에 나이가 1인 나무 추가한다
    new_tree = []
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for a, b in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                        nr, nc = i+a, j+b
                        if 0<=nr<N and 0<=nc<N:
                            trees[nr][nc].append(1)
    # 겨울 - 로봇이 돌아다니며 A[r][c]만큼 양분을 추가한다
            board[i][j] += A[i][j]

alive_tree_cnt = 0
for i in range(N):
    for j in range(N):
        alive_tree_cnt += len(trees[i][j])

print(alive_tree_cnt)