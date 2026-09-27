class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        candidates = sorted(candidates)

        def backtrack(i, total):
            if total == target and path.copy() not in results:
                results.append(path.copy())
                return
            if i >= len(candidates) or total > target:
                return

            total += candidates[i]
            path.append(candidates[i])

            backtrack(i + 1, total)

            total -= candidates[i]
            path.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return results
