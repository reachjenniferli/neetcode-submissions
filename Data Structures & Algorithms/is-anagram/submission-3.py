class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schars = defaultdict(int)
        tchars = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in s:
            schars[i] += 1
        
        for i in t:
            tchars[i] += 1
        
        if tchars == schars:
            return True
        else:
            return False