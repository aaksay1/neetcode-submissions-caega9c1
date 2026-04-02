class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def dfs(i, j, curr):
            if curr == len(word):
                return True
            
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[curr]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"  

            found = (dfs(i+1, j, curr+1) or
                    dfs(i-1, j, curr+1) or
                    dfs(i, j+1, curr+1) or
                    dfs(i, j-1, curr+1))
            
            board[i][j] = temp   
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
        
