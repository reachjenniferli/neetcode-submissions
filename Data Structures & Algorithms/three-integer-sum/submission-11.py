class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        resset = set()
        res = []

        for i, n in enumerate(nums):
            l = i + 1
            r = len(nums)-1
            if nums[i] > 0:
                break
            while r > l:
                if nums[l]+nums[r]==-nums[i]:
                    if (nums[l], nums[r], nums[i]) not in resset:
                        resset.add((nums[l], nums[r], nums[i]))
                        res.append([nums[l], nums[r], nums[i]])
                    r -= 1
                    l += 1
                    continue
                elif nums[l]+nums[r]<-nums[i]:
                    l += 1
                elif nums[l]+nums[r]>-nums[i]:
                    r -= 1

        return res