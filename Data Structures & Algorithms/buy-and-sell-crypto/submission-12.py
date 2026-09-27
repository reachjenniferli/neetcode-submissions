class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        
        l = 0
        r = 1
        profit = 0
        
        while r < len(prices)-1:
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = max(profit, prices[r]-prices[l])
                r += 1
        profit = max(profit, prices[r]-prices[l])

        return profit