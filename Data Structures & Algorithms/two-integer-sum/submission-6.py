class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNums = dict()
        for i in range(len(nums)):
            if target - nums[i] in dictNums:
                return [dictNums[target-nums[i]], i]
            dictNums[nums[i]] = i
