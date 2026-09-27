class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adds = defaultdict(int)

        for i, n in enumerate(nums):
            if target - n in adds:
                return [adds[target-n], i]
            adds[n] = i