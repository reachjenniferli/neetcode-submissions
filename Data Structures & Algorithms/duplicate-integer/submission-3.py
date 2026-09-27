class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appears = set()

        for i in nums:
            if i in appears:
                return True
            appears.add(i)
        return False