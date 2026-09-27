class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = 0

        while l < r:
            m = l + (r-l)//2
            res = 0
            for i in piles:
                res += (i + m - 1) // m
            if res <= h:
                r = m
            elif res > h:
                l = m + 1

        return l