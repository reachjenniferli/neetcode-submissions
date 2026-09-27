class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize dictionary
        res = [0]
        #keep track lowest
        #keep track highest
        #subtract highest from lowest
        left = 0
        right = 1
        cur = 0
        i = 0

        for i in range(len(prices)):
            if right == len(prices):
                break
            #print(prices[right])
            #print(prices[left])
            cur = prices[right] - prices[left]
            # two pointers
            if res[-1] > cur:
                if prices[right] < prices[left]:
                    left = i+1
                    right += 1
                    #print('a')
                elif prices[right] >= prices[left]:
                    right += 1
                    #print('b')

            else: 
                right += 1
                res.append(cur)
                #print('c')

            #print(res)

        return res[-1]
