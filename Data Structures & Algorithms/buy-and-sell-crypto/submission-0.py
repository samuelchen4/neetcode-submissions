class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # compare if current value is smaller than l

        l = 0
        result = 0

        for r in range(len(prices)):
            result = max(result, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            
        return result