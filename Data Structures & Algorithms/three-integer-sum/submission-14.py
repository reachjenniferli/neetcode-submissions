class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []

        for i, n in enumerate(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while r > l:
                if nums[l]+nums[r]==-nums[i]:
                    res.append([nums[l], nums[r], nums[i]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l]+nums[r]<-nums[i]:
                    l += 1
                elif nums[l]+nums[r]>-nums[i]:
                    r -= 1

        return res