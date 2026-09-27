class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        M = L + R // 2
        minimum = float('inf')

        if nums[R] > nums[L]:
            return nums[L]

        while L <= R:
            curr = nums[M]
            print(curr)

            if curr <= minimum:
                if nums[R] < curr:
                    L = M + 1
                else: 
                    R = M - 1
                minimum = curr
                

            elif curr > minimum:
                L = M + 1

            M = (L + R) // 2

        return minimum