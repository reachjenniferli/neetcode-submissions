class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        l = 0
        freq = 0
        res = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            freq = max(chars.values())
            while k < r-l+1-freq:
                chars[s[l]] -= 1
                l += 1
                freq = max(chars.values())
            res = max(res, r-l+1)

        return min(res, len(s))

        
