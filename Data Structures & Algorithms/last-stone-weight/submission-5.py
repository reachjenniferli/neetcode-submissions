class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            heapq.heappush(heap, -abs(x-y))
            print(heap)
        
        return abs(heap[0])
