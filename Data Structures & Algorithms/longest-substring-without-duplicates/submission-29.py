class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        chars = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if s[r] in chars:
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1
            else:
                chars.add(s[r])
                res = max(res, r-l)
            r += 1
        return res+1
