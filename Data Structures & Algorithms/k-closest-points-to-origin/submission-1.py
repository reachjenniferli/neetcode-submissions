class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i in range(len(points)):
            distance = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(minHeap, (distance, i))

        result = []

        while len(result) < k:
            result.append(points[(heapq.heappop(minHeap))[1]])

        print(result)

        return result