class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #storing ints (key) and corresponding frequencies (value)
        nums_freq = defaultdict(int)
        #storing corresponding frequences (key) and ints (value)
        find = defaultdict(list)

        #iterate through list
        for i in nums: 
            #remove prev int position on freq list
            if nums_freq[i] > 0:
                find[nums_freq.get(i)].remove(i)
            #update freq for the int
            nums_freq[i] += 1
            #add new int position on freq list
            find[nums_freq.get(i)].append(i)
            #print(find)

        #add to result array
        res = []
        while len(res) < k:
            ls = (find.get(max(find)))
            res.extend(ls)
            find.pop(max(find))
            #print(res)

        return res[:k]
        

