class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chars = set()

        for i in nums:
            if i in chars:
                return True
            else:
                chars.add(i)

        return False