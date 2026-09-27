class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for n in stones:
            heapq.heappush(maxHeap, -n)

        while len(maxHeap) > 1:
            largest = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            
            if largest > second:
                heapq.heappush(maxHeap, -(largest-second))
        
        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        else:
            return 0
        
        