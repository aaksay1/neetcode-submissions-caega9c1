class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0
        mins = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:

            for _ in range(len(q)):
                    i, j = q.popleft()

                    for di, dj in directions:
                        ni = di + i
                        nj = dj + j

                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            fresh -= 1
                            q.append((ni, nj))

            mins += 1  

        if fresh > 0:
            return - 1      

        return mins

