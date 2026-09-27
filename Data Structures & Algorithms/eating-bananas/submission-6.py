class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        output = R

        while L <= R:
            M = (L+R)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/M)
            
            if hours <= h:
                output = M
                R = M - 1

            else: # res < h
                L = M + 1

        return output