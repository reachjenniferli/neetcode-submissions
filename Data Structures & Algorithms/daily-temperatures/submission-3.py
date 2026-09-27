class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = []
        res = [0] * len(temperatures)
        pop = 0

        for i, n in enumerate(temperatures):
            for a in range(len(ls)):
                if temperatures[ls[a-pop]] < n:
                    res[ls[a-pop]] = i - ls[a-pop]
                    ls.pop(a-pop)
                    pop += 1
            pop = 0
            ls.append(i)

            print(ls)
            print(res)
        
        return res