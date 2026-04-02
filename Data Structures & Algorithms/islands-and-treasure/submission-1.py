class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid) # rows
        n = len(grid[0]) # cols

        q = deque() # all the reasures

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            i, j = q.popleft()
            for di, dj in directions:
                
                ni = di + i
                nj = dj + j

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 2147483647:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))
            



