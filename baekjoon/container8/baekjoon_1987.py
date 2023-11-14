import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x:int,y:int):
    global result
    stack = [(x,y,board[x][y])]
    while stack:
        r, c, root = stack.pop()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<R and 0<=nc<C and board[nr][nc] not in root:
                stack.append((nr,nc,root+board[nr][nc]))
                result = max(result, len(root)+1)
                if result >= 26:
                    exit()
                    return

result = 1
dfs(0,0)
print(result)