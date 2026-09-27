class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = 0
        R = 1
        current = 0
        output = 0

        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
            else:
                current = prices[R] - prices[L]
                output = max(output, current)

            R += 1

        return output
