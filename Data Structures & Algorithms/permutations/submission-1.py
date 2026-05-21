class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            for num in nums:
                if num in arr:
                    continue

                arr.append(num)
                backtrack(arr)
                arr.pop()
        
        backtrack([])

        return res