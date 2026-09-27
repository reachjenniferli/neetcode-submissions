class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for n in points:
            distance = n[0]*n[0] + n[1]*n[1]

            heapq.heappush(maxHeap, (-distance, n))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        for n in maxHeap:
            result.append(n[1])

        return result