class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        klargest = defaultdict(list)
        kdict = defaultdict(int)
        res = []

        for i in nums:
            kdict[i] += 1
        
        for i in kdict:
            klargest[kdict[i]].append(i)

        print(klargest)
        print(kdict)
        
        for i in range(max(klargest), 0, -1):
            for a in klargest[i]:
                res.append(a)
                if len(res) == k:
                    return res


