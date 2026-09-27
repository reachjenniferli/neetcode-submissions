class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sequences = defaultdict()
        highest = 0

        for i, n in enumerate(nums):
            
            if (n - 1) in nums:
                continue
            
            x = n
            current = 0

            while (x in nums):
                current += 1
                x += 1
            
            if current > highest:
                highest = current

        return highest