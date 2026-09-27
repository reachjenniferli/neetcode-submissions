class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width = 0
        height = 0
        max_amount = width * height

        for l in range(len(heights)):
            r = len(heights) - 1
            while r > l:
                h = min(heights[r], heights[l])
                area = (r-l) * h
                print(r)
                print(l)
                print(h)
                print(area)
                print("_____")
                max_amount = max(max_amount, area)
                r -= 1
        return max_amount