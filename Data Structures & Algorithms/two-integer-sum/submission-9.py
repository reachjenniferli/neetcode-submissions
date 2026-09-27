class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        add = dict()

        for i in range(len(nums)):
            add[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in add and i != add[target-nums[i]]:
                return [i, add[target - nums[i]]]