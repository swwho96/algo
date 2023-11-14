import sys
input = sys.stdin.readline
N = int(input())

board = []
K = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    K = max(K, max(tmp))
    board.append(tmp)

sinked = [[0] * N for _ in range(N)]
result = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    sinked[x][y] = 0
    stack = [(x,y)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<N and 0<=nc<N and sinked[nr][nc] == 1:
                sinked[nr][nc] = 0
                stack.append((nr,nc))

for k in range(1,K+1):
    # 물에 잠기는 지역 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] > k:
                sinked[i][j] = 1
    
    # 잠기지 않은 영역 확인
    cnt = 0
    for i in range(N):
        for j in range(N):
            if sinked[i][j] == 1:
                bfs(i, j)
                cnt += 1
    result = max(result,cnt)

print(result)