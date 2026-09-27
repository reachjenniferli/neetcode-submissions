class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = 0
        heap = []

        while r < k:
            heapq.heappush(heap, -nums[r])
            r += 1
        res.append(-heap[0])

        while r < len(nums):
            heap.remove(-nums[l])
            heap.append(-nums[r])
            heapq.heapify(heap)
            res.append(-heap[0])
            r += 1
            l += 1

        return res


