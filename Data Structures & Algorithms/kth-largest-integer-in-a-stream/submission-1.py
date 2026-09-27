class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        heap = self.nums
        heapq.heapify(heap)
        heapq.heappush(heap, val)
        while len(heap) > self.k:
            heapq.heappop(heap)
        return heap[0]