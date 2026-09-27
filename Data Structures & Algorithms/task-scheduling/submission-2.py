class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap = []

        # X X Y Y n = 2
        # A A A B C n = 3
        # A B C idle A idle idle idle A
        # most frequent letter controls length
        # A A A B B B C n = 2
        # A _ A _ A _ _
        # 1 find most freq letter
        # 2 spread out letters letters-1 * n + 1
        # 3 add how many of the rest of the letters are left
        # length - letters-1 * n + 1
        
        count = Counter(tasks)
        maxheap = [-i for i in count.values()]
        
        heapq.heapify(maxheap)

        print(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time += 1
            if maxheap:
                recent = -heapq.heappop(maxheap) - 1
                if recent:
                    q.append([recent, time + n])
            if q and q[0][1] <= time:
                heapq.heappush(maxheap, -q.popleft()[0])

        return time
        
