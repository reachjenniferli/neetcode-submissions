class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = 0
        heap = []

        while r < k:
            heapq.heappush(heap, (-nums[r], r))
            r += 1
        res.append(-heap[0][0])

        while r < len(nums):
            while heap and heap[0][1] <= l:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[r], r))
            res.append(-heap[0][0])
            r += 1
            l += 1

        return res