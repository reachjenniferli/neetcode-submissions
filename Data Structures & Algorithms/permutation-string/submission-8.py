class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = Counter(s1)
        l = 0
        r = len(s1)
        chars2 = Counter(s2[l:r])
        print(chars2)
        if chars2 == chars1:
                return True
        
        while r < len(s2):
            chars2[s2[r]] += 1
            chars2[s2[l]] -= 1
            if chars2[s2[l]] == 0:
                del chars2[s2[l]]
            if chars2 == chars1:
                return True
            r += 1
            l += 1

            print(chars2)

        return False