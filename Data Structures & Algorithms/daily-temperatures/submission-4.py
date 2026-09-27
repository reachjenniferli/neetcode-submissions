class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = []
        res = [0] * len(temperatures)
        a = 0
        pop = 0

        for i, n in enumerate(temperatures):
            while ls and n > temperatures[ls[-1]]:
                if temperatures[ls[-1]] < n:
                    res[ls[-1]] = i - ls[-1]
                    ls.pop(-1)
                    pop += 1
                    a += 1
            pop = 0
            ls.append(i)

            #print(ls)
            #print(res)
        
        return res