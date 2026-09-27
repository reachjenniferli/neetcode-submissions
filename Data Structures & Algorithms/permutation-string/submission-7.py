class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = Counter(s1)
        l = 0
        r = len(s1)
        
        while r < len(s2)+1:
            chars2 = Counter(s2[l:r])
            if chars2 == chars1:
                return True
            r += 1
            l += 1

        return False