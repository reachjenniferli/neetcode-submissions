class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        print(nums)
        current = 1
        longest = 1
        prev = nums[0]
        #if key - 1 exists
        for i in range(len(nums)):
            if prev == nums[i]:
                continue
            if prev + 1 == nums[i]:
                current += 1
            else:
                if current > longest:
                    longest = 0
                    longest += current + 0
                current = 1
            prev = nums[i]

        if current > longest:
            longest = 0
            longest += current + 0
        #return 
        return longest
        