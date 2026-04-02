class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left_side = [1] * n
        right_side = [1] * n

        curr = 1

        for i in range(n):
            left_side[i] = curr
            curr *= nums[i]
        
        curr = 1

        for i in range(n - 1, -1, -1):
            right_side[i] = curr
            curr *= nums[i]
        
        res = []
        for i in range(n):
            res.append(right_side[i] * left_side[i])
        
        return res