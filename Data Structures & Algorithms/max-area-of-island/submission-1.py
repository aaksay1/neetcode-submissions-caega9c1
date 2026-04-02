class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        curr = 0
        res = 0

        def traverse(i, j):
            if (i < 0 or j < 0 or m <= i or n <= j or grid[i][j] == 0):
                return
            
            nonlocal curr

            curr += 1
            grid[i][j] = 0
            
            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    traverse(i, j)
                    res = max(curr, res)
                    curr = 0
        
        return res