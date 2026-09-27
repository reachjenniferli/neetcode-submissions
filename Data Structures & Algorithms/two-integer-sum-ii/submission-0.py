class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target - i in numbers:
                index1 = numbers.index(target-i)+1
                index2 = numbers.index(i)+1
                return [min(index1, index2), max(index1, index2)]