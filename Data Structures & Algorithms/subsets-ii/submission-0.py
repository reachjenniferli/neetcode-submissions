class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                if path not in results:
                    results.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i+1)

            path.pop()
            while (i+1)<len(nums) and nums[i]==nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return results
