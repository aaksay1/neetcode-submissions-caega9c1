class Solution:
    def solve(self, board: List[List[str]]) -> None:
        good_Os = set()

        m = len(board)
        n = len(board[0])

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            
            visited.add((i, j))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for di, dj in directions:
                ni = di + i
                nj = dj + j

                if(0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O"):
                    dfs(ni, nj, visited)

        for c in range(n):  # top row
            if(board[0][c] == "O"):
                dfs(0, c, good_Os)
        for r in range(m):  # left column
            if(board[r][0] == "O"):
                dfs(r, 0, good_Os)

        for c in range(n):  # bottom row
            if(board[m-1][c] == "O"):
                dfs(m-1, c, good_Os)
        for r in range(m):  # right column
            if(board[r][n-1] == "O"):
                dfs(r, n-1, good_Os)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in good_Os:
                    board[i][j] = "X"

        