class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0
        R = len(nums)-1
        M = (L+R)//2
        shift = 0

        while nums[R-shift] < nums[L-shift]:
            shift += 1
            print(nums[L-shift])
            print(nums[R-shift])
            print('hihihihi')

        #if nums[L] == target:
        #    return L
            
        while L <= R:
            M = (R+L)//2
            curr = nums[M-shift]
            print(L)
            print(M)
            print(R)
            print(curr)
            print('____')

            if curr == target:
                return ((M-shift)+len(nums))%len(nums)

            elif curr > target:
                R = M - 1
            
            elif curr < target:
                L = M + 1

        return -1

