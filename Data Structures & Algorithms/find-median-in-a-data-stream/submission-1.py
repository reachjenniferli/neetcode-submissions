class MedianFinder:

    def __init__(self):
        self.datastream = []

    def addNum(self, num: int) -> None:
        self.datastream.append(num)

    def findMedian(self) -> float:
        if len(self.datastream) == 1:
            return self.datastream[0]

        length = len(self.datastream)

        minheap = []

        for num in self.datastream:
            heapq.heappush(minheap, num)

        if length%2 == 1:
            for i in range(length//2 + 1):
                    median = heapq.heappop(minheap)
        else:
            for i in range(length//2):
                median = heapq.heappop(minheap)
            median += heapq.heappop(minheap)
            median = median / 2

        return median


        