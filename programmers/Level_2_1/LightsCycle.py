def solution(grid):
    R, C = len(grid), len(grid[0])
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]


    def solve(x, y, d):
        res = 0
        while not visited[x][y][d]:
            visited[x][y][d] = 1
            x, y = (x+direction[d][0]) % R, (y+direction[d][1]) % C
            if grid[x][y] == 'L': d = (d+1) % 4
            elif grid[x][y] == 'R': d = (d-1) % 4
            res += 1
        return res


    ans = []
    for i in range(R):
        for j in range(C):
            for k in range(4):
                if visited[i][j][k] == 0:
                    ans.append(solve(i, j, k))             
    return sorted(ans)