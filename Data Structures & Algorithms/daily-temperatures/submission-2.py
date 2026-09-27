class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = 0

        for i in range(len(temperatures)):
            while (i+n) < len(temperatures) and temperatures[i+n] <= temperatures[i]:
                n += 1
            if i+n >= len(temperatures):
                result.append(0)
            else: result.append(n)
            n = 0
        
        return result
