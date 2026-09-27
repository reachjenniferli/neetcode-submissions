class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []
        path = []

        def backtrack(i, total):
            if total == target:
                results.append(path.copy())
                return
            
            if total > target or i >= len(nums):
                return

            total += nums[i]
            path.append(nums[i])

            backtrack(i, total)

            total -= nums[i]
            path.pop()

            backtrack(i+1, total)

        backtrack(0, 0)
        return results
            