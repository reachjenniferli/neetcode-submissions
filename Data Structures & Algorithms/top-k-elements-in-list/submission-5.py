class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        klargest = []
        kdict = defaultdict(int)

        for i in nums:
            kdict[i] += 1
        
        for i in kdict:
            if len(klargest) < k:
                heapq.heappush(klargest, (kdict[i], i))
            else:
                if int(klargest[0][0]) < kdict[i]:
                    heapq.heappop(klargest)
                    heapq.heappush(klargest, (kdict[i], i))

        return [tup[1] for tup in klargest]