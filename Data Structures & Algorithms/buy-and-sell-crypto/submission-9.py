class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0

        while right < len(prices)-1 and left <= right:
            if prices[left] > prices[right]:
                left = right
            else: 
                right += 1
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]

        return profit
