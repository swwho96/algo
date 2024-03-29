# 재귀를 활용한 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt


# 반복을 활용한 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # DFS
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop(0)
                        for nx, ny in zip([-1,1,0,0], [0,0,-1,1]):
                            if 0<=x+nx<m and 0<=y+ny<n and grid[x+nx][y+ny] == '1':
                                stack.append((x+nx, y+ny))
                                grid[x+nx][y+ny] = '#'
                    island += 1
        return island