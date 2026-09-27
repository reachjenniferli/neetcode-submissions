class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        res = nums[0]

        while L <= R:
            if nums[R] > nums[L]:
                res = min(res, nums[L])
                break

            M = (L + R) // 2
            curr = nums[M]
            res = min(res, curr)

            if curr >= nums[L]:
                L = M + 1
            else: 
                R = M - 1

        return res