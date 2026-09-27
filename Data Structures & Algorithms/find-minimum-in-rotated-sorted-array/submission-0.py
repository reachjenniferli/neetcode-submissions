class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = -1
        while nums[r] < nums[l]:
            m = ((r % len(nums)) + l) // 2
            while nums[l] > nums[m] or nums[l] > nums[r]:
                minOf = min(nums[m], nums[r])
                l = nums.index(minOf)
            r = (l - 1) % -(len(nums))
            print(nums[l])
            print(nums[m])
            print(nums[r])
            print("__")
            

        return nums[l]
        