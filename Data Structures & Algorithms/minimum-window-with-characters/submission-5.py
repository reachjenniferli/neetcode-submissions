class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = Counter(t)
        res = ""
        l = 0
        needed = len(chars)

        for r in range(len(s)):
            if s[r] not in chars:
                continue
            chars[s[r]] -= 1
            if chars[s[r]] == 0:
                needed -= 1
            while needed == 0 and l <= r:
                if res == "" or r-l+1 < len(res):
                    res = s[l:r+1]
                if s[l] in chars:
                    chars[s[l]] += 1
                    if chars[s[l]] > 0:
                        needed += 1
                l += 1
            
        return res
        