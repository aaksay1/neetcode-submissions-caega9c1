class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        low = 1

        res = hi

        while(hi >= low):
            mid = (low + hi) // 2
            
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            
            if total_time <= h:
                res = min(res, mid)
                hi = mid - 1
            else:
                low = mid + 1
        
        return res