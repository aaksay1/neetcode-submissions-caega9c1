class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) # rows
        n = len(heights[0]) # cols

        pacific = set()
        atlantic = set()
        res = []

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            
            visited.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for di, dj in directions:
                ni = di + i
                nj = dj + j

                if(0 <= ni < m and 0 <= nj < n and heights[i][j] <= heights[ni][nj]):
                    dfs(ni, nj, visited)

        # left side, pacific
        for i in range(m):
            dfs(i, 0, pacific)

        # top side, pacific
        for j in range(n):
            dfs(0, j, pacific)

        # right side, atlantic
        for i in range(m):
            dfs(i, n-1, atlantic)

        # bottom side, atlantic
        for j in range(n):
            dfs(m-1, j, atlantic)

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append((i, j))
        
        return res