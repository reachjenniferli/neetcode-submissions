class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        setnums = set()
        output = 0

        for end in range(len(s)):
            while s[end] in setnums:
                setnums.remove(s[start])
                start += 1
            setnums.add(s[end])
            if len(setnums) > output:
                output = len(setnums)

        return output
