class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length == 0 or num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)

        print(self.small)
        print(self.big)

        if len(self.small) > len(self.big)+1:
            biggest = heapq.heappop(self.small)
            heapq.heappush(self.big, -biggest)
        elif len(self.big) > len(self.small)+1:
            smallest = heapq.heappop(self.big)
            heapq.heappush(self.small, -smallest)

        print(self.small)
        print(self.big)
        self.length+= 1

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (-self.small[0]+self.big[0])/2
        elif len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return self.big[0]



        