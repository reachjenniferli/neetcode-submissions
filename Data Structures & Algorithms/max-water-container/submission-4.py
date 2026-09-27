class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L = 0
        R = len(heights) - 1
        highest = 0
        current = 0

        while L < R:

            smaller = min(heights[L], heights[R])

            current = smaller * (R - L)

            if current > highest: 
                highest = current

            if heights[R] == smaller: 
                R -= 1
            else: 
                L += 1
                
            print(highest)

        return highest