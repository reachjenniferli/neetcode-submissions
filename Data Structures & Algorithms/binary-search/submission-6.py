class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        M = len(nums) // 2
        curr = nums[M]
        if target == nums[R]:
            return R
        if target == nums[L]:
            return L

        while M != R and M != L:
            print(nums[L])
            print(nums[M])
            print(nums[R])
            curr = nums[M]
            print(curr)
            print('_______')

            if curr == target:
                return M

            elif curr > target:
                R = M

            else:
                L = M
            
            M = (R-L) // 2 + L

        return -1