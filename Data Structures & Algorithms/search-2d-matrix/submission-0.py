class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0]) 

        needed_row = -1
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                needed_row = i
                break
        if needed_row == -1:
            return False

        # Binary search in that row
        low = 0
        hi = n - 1
        while low <= hi:
            mid = (low + hi) // 2
            curr = matrix[needed_row][mid]
            if curr == target:
                return True
            elif curr < target:
                low = mid + 1
            else:
                hi = mid - 1

        return False

