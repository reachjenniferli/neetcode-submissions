class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = defaultdict(int)

        for n in nums: 
            values[n] += 1

        answer = []

        for i in range(k):
            answer.append(max(values, key = values.get))
            values.pop(max(values, key = values.get))

            if len(answer) == k:
                return answer