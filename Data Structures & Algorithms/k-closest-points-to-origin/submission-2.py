class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for n in points:
            distance = math.sqrt((n[0])**2 + (n[1])**2)
            heapq.heappush(minHeap, (distance, n))

        result = []

        while len(result) < k:
            result.append((heapq.heappop(minHeap))[1])

        print(result)

        return result