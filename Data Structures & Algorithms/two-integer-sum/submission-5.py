class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = i + 1
            for a in range(len(nums)-i-1):
                if nums[i] + nums[x] == target:
                    return [i, x]
                x += 1