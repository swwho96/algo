from collections import deque
def solution(board):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(board, dir):
        n = len(board)
        dp = [[int(1e9)]*n for _ in range(n)]
        dp[0][0] = 0
        q = deque([(0,0,0,dir)])
        while q:
            x, y, cost, d = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = i
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                    if nd == d:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600
                    if ncost < dp[nx][ny]:
                        dp[nx][ny] = ncost
                        q.append((nx,ny,ncost,i))
        return dp[-1][-1]
    
    return min(bfs(board, 1), bfs(board, 3))