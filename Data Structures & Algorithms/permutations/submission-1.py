class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        used = set()

        def dfs(subset, used):
            if len(subset) == len(nums):
                results.append(subset.copy())
            for i in nums:
                if i not in used:
                    subset.append(i)
                    used.add(i)
                    dfs(subset, used)
                    subset.pop()
                    used.remove(i)

        dfs(subset, used)
        return results


