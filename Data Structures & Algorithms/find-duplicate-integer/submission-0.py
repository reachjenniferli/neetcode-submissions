class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        duplicates = set()

        for a in nums:
            if a in duplicates:
                return a
            else: duplicates.add(a)