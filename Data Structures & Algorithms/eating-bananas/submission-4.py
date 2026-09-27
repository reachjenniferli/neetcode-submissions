class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        maximum = max(piles)
        R = maximum
        M = math.ceil((R-L)/2)
        res = 0
        output = -1

        for i in piles:
            res += math.ceil(i)
            
        if res <= h:
            return 1
        
        print(L)
        print(M)
        print(R)
        res = 0

        while M!=L and M!=R:
            for i in piles:
                res += math.ceil(i/M)
            print(M)
            print(res)
            print(output)
            
            if res <= h:
                output = M
                R = M

            else: # res < h
                L = M

            M = math.ceil((R-L)/2 + L)
            res = 0

        if output == -1: return maximum
        else: return output