class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            heapq.heappush(heap, (-math.sqrt((points[i][0])**2 + (points[i][1])**2), points[i]))
            print(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        result = []

        for i in range(len(heap)):
            result.append(heap[i][1])

        return result