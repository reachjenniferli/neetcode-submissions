class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        seen = defaultdict(int)

        for i in sorted(nums):
            if i-1 in seen:
                seen[i] = seen[i-1] + 1
            else:
                seen[i] = 1
        
        return max(seen.values())