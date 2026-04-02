class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        hi = len(nums) - 1

        while(hi > low):
            mid = (low + hi) // 2

            if nums[mid] > nums[hi]:
                low = mid + 1
            else:
                hi = mid
            
        return nums[low]
