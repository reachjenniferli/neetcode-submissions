class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxl = height[0]
        maxr = height[len(height)-1]
        l = 0
        r = len(height)-1
        res = 0
        
        while maxl == height[l] and r > l:
            l += 1
            maxl = max(height[l], maxl)
            

        while maxr == height[r] and r > l:
            r -= 1
            maxr = max(height[r], maxr)

        print(l)
        print(r)
        print(maxl)
        print(maxr)

        while r > l:
            if maxl < maxr:
                res += maxl - height[l]
                l += 1
            else:
                res += maxr - height[r]            
                r -= 1
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)


        res += min(maxr, maxl) - height[l]

        return res