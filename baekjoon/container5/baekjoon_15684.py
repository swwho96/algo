import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

def check():
    for i in range(1, N+1):
        now = i
        for b in board:
            if b[now-1] == 1:
                now -= 1
            elif b[now] == 1:
                now += 1
        if i != now:
            return False
    return True

def dfs(depth, i):
    global result
    if depth >= result:
        return
    if check():
        result = depth
        return
    for c in range(i, len(combi)):
        x, y = combi[c]
        if board[x][y-1] == 0 and board[x][y+1] == 0:
            board[x][y] = 1
            dfs(depth+1, c+1)
            board[x][y] = 0

combi = []
for i in range(1, H+1):
    for j in range(1, N):
        if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
            combi.append((i,j))

result = 4
dfs(0, 0)
print(result if result < 4 else -1)