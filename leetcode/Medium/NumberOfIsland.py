List = list
from collections import deque
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


        visited = []
        queue = deque([(1,1)])    
        cnt = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # dfs(i, j)
                    # cnt += 1
        
                while queue:

        
        
        
        
        
        return cnt