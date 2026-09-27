class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        for i in range(len(nums)):
            m = (l + r) // 2
            if nums[(m-1)%len(nums)] > nums[m] and nums[(m+1)%len(nums)] > nums[m]:
                return nums[m]
            if nums[r] > nums[m]:
                r = m-1
            elif nums[r] < nums[m]:
                l = m+1

            #print(nums[l])
            #print(nums[m])
            #print(nums[r])
            #print("___")
        return nums[m]

        