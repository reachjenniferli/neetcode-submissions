class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        r, l = 0, 0
        chars = defaultdict(int)
        freq = s[0]
        substring = 1

        while r < len(s):
            chars[s[r]] += 1
            if s[r] != freq and chars[s[r]] > chars[freq]:
                    freq = s[r]
            while r-l+1 - chars[freq] > k:
                chars[s[l]] -= 1
                l += 1
                for i in chars:
                    if chars[i] > chars[freq]:
                        freq = i
            substring = max(substring, r-l+1)
            r += 1
            #print(chars)
            #print(freq)
            #print(substring)

        return substring