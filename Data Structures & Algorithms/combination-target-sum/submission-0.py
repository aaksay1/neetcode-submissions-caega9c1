class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtracking(start_index, path, remaining_target):
            if remaining_target == 0:
                res.append(path[:])
                return
            
            if remaining_target < 0:
                return
            
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(i, path, remaining_target - nums[i])
                path.pop()
        
        backtracking(0, [], target)

        return res