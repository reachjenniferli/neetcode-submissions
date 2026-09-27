class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = 0
        R = len(prices) - 1
        buy = 0
        sell = 0
        selldate = 0
        output = 0

        for i, price in enumerate(prices):
            if price < prices[buy]:
                buy = i
            elif price >= prices[sell]: 
                sell = i

            if buy > sell:
                buy = i
                sell = i

            output = max(output, (prices[sell]-prices[buy]))
            print(output)

        return output


            

