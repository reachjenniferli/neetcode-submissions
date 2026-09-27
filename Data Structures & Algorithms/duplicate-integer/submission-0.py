class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in range (len(nums)):
            if nums[i] in nums_dict:
                return True
            nums_dict[nums[i]] = i
        return False