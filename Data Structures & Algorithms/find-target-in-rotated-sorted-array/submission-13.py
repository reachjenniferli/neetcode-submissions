class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0
        R = len(nums)-1
        M = (L+R)//2
            
        while L <= R:
            M = (R+L)//2
            curr = nums[M]
            print(L)
            print(M)
            print(R)
            print(curr)
            print('____')

            if curr == target:
                return M

            elif curr >= nums[L]:
                if nums[L] <= target < curr:
                    R = M - 1
                else:
                    L = M + 1
            
            elif curr <= nums[R]:
                if nums[R] >= target > curr:
                    L = M + 1
                else:
                    R = M - 1


        return -1

