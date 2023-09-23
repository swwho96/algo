def check(b, x, y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4): # 상하좌우
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<5 and 0<=ny<5 and b[nx][ny] == 'P':
            return False
        if 0<=nx+dx[i]<5 and 0<=ny+dy[i]<5 and b[nx][ny] == 'O' and b[nx+dx[i]][ny+dy[i]] == 'P':
            return False
    for i,j in [(-1,-1), (-1,1), (1,-1), (1,1)]: # 대각선
        nx, ny = x+i, y+j
        if (0<=nx<5 and 0<=ny<5 and b[nx][ny] == 'P') and (b[nx][y] == 'O' or b[x][ny] == 'O'):
            return False
    return True

def solution(places):
    answer = []
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(place, i,j):
                        flag = 0
                        break
            if flag == 0:
                break
        answer.append(flag)
    return answer

# --------------------------------------------------------------------------------------------------------

def solution(places):
    answer = []
    
    def dfs(room, row, col, dist):
        nonlocal flag
        if dist == 2:
            return 
        visited[row][col] = True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nrow, ncol = row + dx, col + dy
            if 0 <= nrow < 5 and 0 <= ncol < 5:
                if room[nrow][ncol] == 'P' and visited[nrow][ncol] is False:
                    flag = 0
                    return
                if room[nrow][ncol] == 'O' and visited[nrow][ncol] is False:
                    dfs(room, nrow, ncol, dist + 1)
                    
    for place in places:
        flag = 1
        visited = [[False] * 5 for _ in range(5)]
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    dfs(place, r, c, 0)
        answer.append(flag)
    return answer