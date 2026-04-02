class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0

        for i in range(len(prices)):
            res = max(res, prices[i] - prices[buy])

            if prices[i] < prices[buy]:
                buy = i
        
        return res