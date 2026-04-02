class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        def traverse(i, j):
            if(0 > i or i >= m or 0 > j or j >= n or grid[i][j] == "0"):
                return

            grid[i][j] = "0"

            traverse(i + 1, j)
            traverse(i - 1, j)
            traverse(i, j + 1)
            traverse(i, j - 1)


        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1"):
                    traverse(i, j)
                    res += 1

        return res